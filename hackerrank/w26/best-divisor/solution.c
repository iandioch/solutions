#include <stdio.h>
#include <stdlib.h>

int digit_sum(long int n) {
	char buffer[32];
	snprintf(buffer, 32, "%ld", n);
	int i;
	int sum = 0;
	for (i = 0; i < 32; ++i) {
		if (buffer[i] == '\0') break;
		sum += buffer[i] - '0';
	}
	return sum;
}

int main() {
	long int n;
	scanf("%ld", &n);
	long int i;
	long int best = n;
	int best_sum = digit_sum(n);
	for (i = 1; i <= n/2; ++i) {
		if (n % i == 0) {
			int sum = digit_sum(i);
			if ((sum > best_sum) ||
				(sum == best_sum && i < best)) {
				best_sum = sum;
				best = i;
			}
		}
	}
	printf("%ld\n", best);
	return 0;
}
