#include <stdio.h>

int main () {
	long long w = 0;
	long long b = 0;
	while (1) {
		int c = getchar();
		if (c == '\n') {
			break;
		}
		if (c == 'W') ++w;
		if (c == 'B') ++b;
	}
	printf((w==b)?"1\n":"0\n");
	return 0;
}
