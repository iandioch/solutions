#include <stdio.h>

int main() {
	long int n, a, b;
	scanf("%ld %ld %ld", &n, &a, &b);
	long int i = n/a;
	while (1) {
		long int diff = n - (i*a);
		if (diff % b == 0) {
			printf("%ld %ld\n", i, diff / b);
			return 0;
		} else if (i == 0) {
			printf("Impossible");
			return 0;
		} else {
			--i;
		}
	}
	return 0;
}
