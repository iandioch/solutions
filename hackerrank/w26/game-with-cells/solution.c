#include <stdio.h>

/*
*   ...
*   .XX
*   .XX
*/

int main() {
	long int n, m;
	scanf("%ld %ld", &n, &m);
	long int num_across = n/2;
	if (n % 2 == 1) ++num_across;
	long int num_down = m/2;
	if (m % 2 == 1) ++num_down;
	printf("%ld\n", num_across*num_down);
	return 0;
}
