#include <stdio.h>

int main() {
    int n;
    double a, b;
    scanf("%d", &n);
    double r = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%lf %lf", &a, &b);
        r += a*b;
    }
    printf("%lf\n", r);
    return 0;
}
