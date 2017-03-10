#include <stdio.h>
#include <math.h>

int main() {
    while (1) {
        int D;
        long long int v;
        scanf("%d %lld", &D, &v);
        if (D == 0) break;
        double d3 = D*D*D - 6*v/M_PI;
        double d = pow(d3, 1/3.0);
        printf("%.7lf\n", d);
    }
}
