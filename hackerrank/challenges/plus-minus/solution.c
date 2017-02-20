#include <stdio.h>

int main() {
	long int n;
	scanf("%ld", &n);
	long int i;
	long int num_pos = 0;
	long int num_neg = 0;
	long int num_zero = 0;
	for (i = 0; i < n; ++i) {
		long int q;
		scanf("%ld", &q);
		if (q == 0) ++num_zero;
		else if(q > 0) ++num_pos;
		else ++num_neg;
	}

	double fract_pos = ((double) num_pos)/n;
	double fract_neg = ((double) num_neg)/n;
	double fract_zero = ((double) num_zero)/n;

	printf("%lf\n", fract_pos);
	printf("%lf\n", fract_neg);
	printf("%lf\n", fract_zero);
	
	return 0;
}
