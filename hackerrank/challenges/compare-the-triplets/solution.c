#include <stdio.h>

int main () {
	int a = 0;
	int b = 0;

	int i, j, k;
	int l, m, n;

	scanf("%d %d %d", &i, &j, &k);
	scanf("%d %d %d", &l, &m, &n);

	if (i > l) ++a;
	if (j > m) ++a;
	if (k > n) ++a;
	if (i < l) ++b;
	if (j < m) ++b;
	if (k < n) ++b;
	printf("%d %d\n", a, b);
}
