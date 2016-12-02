#include <stdio.h>
#include <string.h>

int main() {
	char in[1000000];
	char out[1000000];
	scanf("%s", in);
	int i = 0, j = 0;
	int n = strlen(in);
	for (; i < n; ++i) {
		if (in[i] == '<') {
			if(j > 0) j--;
		} else {
			out[j] = in[i];
			++j;
		}
	}
	out[j] = '\0';
	printf("%s\n", out);
	return 0;
}
