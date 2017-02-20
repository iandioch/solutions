#include <stdio.h>

int main() {
	int test;
	for (test = 1; test <= 10; ++test) {
		int n;
		scanf("%d", &n);
		if (feof(stdin)) break;
		long int min = 1000001;
		long int max = -1000001;
		int i;
		for (i = 0; i < n; ++i) {
			long int m;
			scanf("%ld", &m);
			if (m < min) min = m;
			if (m > max) max = m;
		}
		printf("Case %d: %ld %ld %ld\n", test, min, max, max-min);
	}
}
