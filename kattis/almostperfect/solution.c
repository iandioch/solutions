#include <stdio.h>
#include <stdlib.h>

int main() {
	unsigned long int n;
	char in[12];
	while (scanf("%12s", in) == 1) {
		n = strtoul(in, NULL, 10);
		unsigned long int d;
		unsigned long long sum = 1L;
		for (d=2; d*d <= n; d ++) {
			if (n % d == 0) {
				sum += d;
				if(d*d != n) {
					sum += n/d;
				}
			}
		}
		if (sum == n) {
			printf("%lu perfect\n", n);
		} else if (llabs(n-sum) <= 2) {
			printf("%lu almost perfect\n", n);
		} else {
			printf("%lu not perfect\n", n);
		}
	}
	return 0;
}
