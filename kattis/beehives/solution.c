#include <stdio.h>
#define sq(a) ((a)*(a))

double x[101];
double y[101];
int sour[101];

int main() {
    while (1) {
        double d;
        int n;
        scanf("%lf %d", &d, &n);
        if (n == 0) break;
        d *= d;
        int i, j;
        for (i = 0; i < n; ++i) {
            sour[i] = 0;
            scanf("%lf %lf", &x[i], &y[i]);
            for (j = 0; j < i; ++j) {
                double dist = sq(x[i] - x[j]) + sq(y[i] - y[j]);
                if (dist <= d) {
                    sour[i] = 1;
                    sour[j] = 1;
                }
            }
        }
        int ans = 0;
        for (i = 0; i < n; ++i) {
            if (sour[i] > 0) {
                ++ans;
            }
        }
        printf("%d sour, %d sweet\n", ans, n-ans);
    }
    return 0;
}
