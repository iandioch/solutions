#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    int ti;
    for (ti = 0; ti < t; ++ti) {
        long int g = 1;
        long long int ans = 0;
        while (g > 0) {
            long int h;
            scanf("%ld", &h);
            if (h > 2*g) {
                ans += h - 2*g;
            }
            g = h;
        }
        printf("%lld\n", ans);
    }
}
