#include <stdio.h>
#include <string.h>

#define LIM 2000000

char sieve[LIM];

void make_sieve() {
	memset(sieve, 1,  sizeof(sieve));
	int i, j;
	for (i = 2; i < LIM; ++i) {
		if (sieve[i]) {
			for (j = i+i; j < LIM; j += i) {
				sieve[j] = 0;
			}
		}
	}
}


int main() {
	make_sieve();
	unsigned long long ans = 0;
	int i;
	for (i = 2; i < LIM; ++i) {
		if (sieve[i]) ans += i;
	}
	printf("%llu\n", ans);
}
