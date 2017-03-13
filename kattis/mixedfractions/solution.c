#include <stdio.h>

int main() {
	while (1) {
		long long int n, d;
		scanf("%lld %lld", &n, &d);
		if (n == 0 && d == 0) {
			break;
		}
		printf("%lld %lld / %lld\n", n/d, n%d, d);
	}
	return 0;
}
