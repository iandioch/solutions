#include <stdio.h>

int main() {
    int ntests;
    scanf("%d", &ntests);
    int test;
    for (test = 0; test < ntests; ++test) {
        int n;
        scanf("%d", &n);
        long double b = 0;
        while (n > 0) {
            b += 0.5;
            b *= 2;
            --n;
        }
        printf("%lld\n", (long long int) b);
    }
    return 0;
}
