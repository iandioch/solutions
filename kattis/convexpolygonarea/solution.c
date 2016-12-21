#include <stdio.h>
#include <string.h>

#define abs(a) (a < 0 ? -a : a)

long double shoelace (int x[], int y[], int n) {
	/* implementation of the shoelace formula */
	long double a = 0, b = 0;
	int i;
	for (i = 0; i < n; ++i) {
		a += x[i] * y[i+1];
		b += y[i] * x[i+1];
	}
	return abs(a-b)/2.0;
}

int main() {
	int num_polys;
	scanf("%d", &num_polys);
	int poly;
	for (poly = 0; poly < num_polys; ++poly) {
		int n;
		scanf("%d", &n);
		int i;
		int x[n+1];
		int y[n+1];
		for (i = 0; i < n; ++i) {
			scanf("%d %d", &x[i], &y[i]);
		}
		x[n] = x[0];
		y[n] = y[0];
		printf("%llf\n", shoelace(x, y, n));
	}
	return 0;
}
