#include <stdio.h>

int c[101];
int d[20000];

int main() {
	int num_tests;
	scanf("%d", &num_tests);
	int test;
	for (test = 0; test < num_tests; ++test) {
		int price, num_coins;
		scanf("%d", &price);
		scanf("%d", &num_coins);
		int i;
		for (i = 0; i < 20000; ++i) {
			d[i] = 0;
		}
		for (i = 0; i < num_coins; ++i) {
			scanf("%d", &c[i]);
		}
		d[0] = 1;
		for (i = 0; i < num_coins; ++i) {
			int j;
			for (j = 19999-c[i]; j >= 0; j --) {
				int nc = d[j];
				if (nc > 0) {
					if (d[j+c[i]] == 0 || nc+1 < d[j + c[i]]) {
						d[j+c[i]] = nc+1;
					}
				}
			}
		}
		for (i = price; ; ++i) {
			if (d[i] > 0) {
				printf("%d %d\n", i, d[i]-1);
				break;
			}
		}
	}
	return 0;
}
