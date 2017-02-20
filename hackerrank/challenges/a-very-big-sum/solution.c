#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long ans = 0;
    long long d;
    int i;
    for (i = 0; i < n; ++i) {
        scanf("%lld", &d);
        ans += d;
    }
    printf("%lld\n", ans);
}
