#include <stdio.h>
#include <math.h>

int main(){
	long int r;
	scanf("%ld", &r);
	long double ca = M_PI*r*r;
	printf("%.6Lf\n", ca);
	long double sa = (r+r)*(r+r)/2;
	printf("%.6Lf\n", sa);
	return 0;
}
