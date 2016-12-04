#include <stdio.h>

int is_prime(long int n) {
	/* assumes odd n */
	if (n % 3 == 0 || n % 5 == 0 || n % 7 == 0) return 0;
	long int i;
	for (i = 11; i*i <= n; i += 2) {
		if (n % i == 0) return 0;
	}
	return 1;
}

int main() {
	long int n, m;
	scanf("%ld %ld", &n, &m);
	long int i;
	if (n < 3) n = 3;
	if (n % 2 == 0) {
		i = n + 1;
	} else {
		i = n;
	}
	long int num_pairs = 0;
	if (n == 3 && m >= 5) {
		++num_pairs;
		n = 5;
	}
	if (n == 5 && m >= 7) {
		++num_pairs;
		n = 11;
	}

	while (is_prime(i) == 0) i += 2;

	while (i <= m - 2) {
		/* invariant: i is prime, i%10 not in {3, 5}*/
		i += 2;
		if (is_prime(i) > 0) {
			num_pairs += 1;
			continue;
		}
		while (is_prime(i) == 0){
			switch (i % 10) {
				/* next i can't end in 3 or 5,
				   as any num > 5 ending in 5
				   is not prime. */
				case 1:
					i += 6;
					break;
				case 3:
					i += 4;
					break;
				default:
					i += 2;
			}
		}
	}
	printf("%ld\n", num_pairs);
	return 0;
}
