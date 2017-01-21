#include <stdio.h>

#define LEN 1000

char n[LEN];

void load_file() {
	FILE* fp;
	fp = fopen("num.txt", "r");

	int i = 0;
	while (i < LEN) {
		char c = fgetc(fp);
		if (c == '\n') continue;
		n[i] = c-'0';
		++i;
	}

	fclose(fp);
}

int main() {
	load_file();

	long long curr = 1;
	long long best = 0;
	int i, j;
	for (i = 0; i < LEN - 13; ++i) {
		curr = n[i];
		for (j = i+1; j < i+13; ++j) {
			curr *= n[j];
		}
		if (curr > best) best = curr;
	}
	printf("%lld\n", best);
}
