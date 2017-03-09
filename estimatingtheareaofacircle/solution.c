#include <stdio.h>
#include <math.h>

int main() {
	while (1) {
		double r;
		long int m, c;
		scanf("%lf %ld %ld", &r, &m, &c);
		if (r == 0) break;

		printf("%.7lf %.7lf\n", M_PI*r*r, 4*r*r*((c+0.0)/m));
	}
	return 0;
}
