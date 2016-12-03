#include <stdio.h>

/*
* a = first value
* d = difference between values
* n = number of series to sum
*/
long long arithmetic_sum (long long a,
	long long d,
	long long n) {
	return n*(2*a + (n-1)*d)/2;
}

int main () {
	long int t;
	scanf("%ld", &t);
	long int i;
	for (i = 0; i < t; ++i) {
		long long n;
		scanf("%lld", &n);
		long long sum = 0;
		sum += arithmetic_sum(3, 3, (n-1)/3);
		sum += arithmetic_sum(5, 5, (n-1)/5);
		sum -= arithmetic_sum(15, 15, (n-1)/15);
		printf("%lld\n", sum);
	}
}
