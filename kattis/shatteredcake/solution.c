#include <stdio.h>

int main() {
    long long int n, w, l;
    long long int tot = 0;
    long long int i;
    scanf("%lld\n", &w);
    scanf("%lld\n", &n);
    long long int a, b;
    for (i = 0; i < n; ++i) {
        scanf("%lld %lld\n", &a, &b);
        tot += a*b;
    }
    l = tot/w;
    printf("%lld\n", l);
    return 0;
}
