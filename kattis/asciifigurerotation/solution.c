#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define max(a,b) a < b ? b : a

int main() {
	char s[5];
	fgets(s, 5, stdin);
	int n = atoi(s);
	while (1) {
		int i, j;

		int lengths[n];
		char lines[n][105];
		int maxlen = 0;
		for (i=0; i < n; ++i) {
			fgets(lines[i], 105, stdin);
			lengths[i] = strlen(lines[i])-1;
			maxlen = max(maxlen, lengths[i]);
		}

		int widths[maxlen];
		for (j = 0; j < maxlen; ++j) {
			widths[j] = 0;
			for (i = n-1; i >= 0; --i) {
				if (j >= lengths[i]) continue;
				if (lines[i][j] == ' ' ||
				    lines[i][j] == '\n') continue;
				widths[j] = i;
			}

		}

		for (j = 0; j < maxlen; ++j) {
			for (i = n-1; i >= 0; --i) {
				if (i < widths[j]) {
					continue;
				}

				if (j >= lengths[i]) {
					printf(" ");
					continue;
				}
				char c = lines[i][j];
				switch (c) {
					case '-': printf("|"); break;
					case '|': printf("-"); break;
					case '\n': printf(" "); break;
					default: printf("%c", c);
				}
			}
			printf("\n");
		}
		fgets(s, 5, stdin);
		n = atoi(s);
		if (n == 0) break;
		printf("\n");
	}
	return 0;
}
