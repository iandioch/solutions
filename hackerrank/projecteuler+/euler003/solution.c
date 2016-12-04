#include <stdio.h>

long int largest_prime_fact (long int m) {
	long int n = m;
	while (n % 2 == 0) n /= 2;
	if (n == 1) return 2;

	long int i = 3;
	long int ans = 3;
	for (i = 3; i*i <= m; i += 2) {
		if (n % i != 0) continue;
		while (n % i == 0) {
			n /= i;
			ans = i;
		}
	}
	if (n > 2) return n;
	return ans;
}

int main() {
	int t;
	scanf("%d", &t);
	int ct;
	for (ct = 0; ct < t; ++ct) {
		long int n;
		scanf("%ld", &n);
		printf("%ld\n", largest_prime_fact(n));
	}
	return 0;
}
