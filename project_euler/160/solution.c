#include <stdio.h>
#define LIM 1000000


int main() {
	long long n = 1000000L*1000000L;

	// the factorial, without zeroes at the end,
	// not including 2s or 5s
	// how many spare 2s there are not matched &
	// cancelled out by 5s (2*5 just adds a zero)
	long long f=1;
	long long n2=0;
	long long i, j;
	for (i = 2; i <= n; ++i) {
		j = i;
		while (j % 2 == 0) {
			j /= 2;
			++n2;
		}
		while (j % 5 == 0) {
			j /= 5;
			--n2;
		}
		f = (f * (j%100000))%1000000;
	}

	printf("all g\n");
	printf("%lld\n", n2);

	for (i = 0; i < n2; ++i) {
		f = (f*2) % 100000;
	}

	printf("%lld\n", f);
	return 0;
}
