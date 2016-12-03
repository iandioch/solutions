#include <stdio.h>

int main() {
	long int t;
	scanf("%ld", &t);
	long int i;
	for (i = 0; i < t; ++i) {
		long long n;
		scanf("%lld", &n);
		long long sum = 0;
		
		long long a = 2;
		long long b = 8;
		while (1) {
			if (a <= n) {
				sum += a;
			} else {
				break;
			}
			long long c = 4*b + a;
			a = b;
			b = c;
		}
		printf("%lld\n", sum);
	}
}
