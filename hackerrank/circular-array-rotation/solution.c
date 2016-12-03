#include <stdio.h>

int main () {
	/* array length, num shifts, num queries */
	long int n, k, q; 
	scanf("%ld %ld %ld", &n, &k, &q);

	long int a[n];
	long int i;
	for (i = 0; i < n; ++i) {
		scanf("%ld", &a[i]);
	}
	for (i = 0; i < q; ++i) {
		long int j;
		scanf("%ld", &j);
		long int real_j = j - k;
		while (real_j < 0) real_j += n;
		printf("%ld\n", a[real_j]);
	}
	
	return 0;
}
