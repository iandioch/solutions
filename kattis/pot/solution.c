#include <stdio.h>

int power(int base, int p) {
    if (p == 0) return 1;
    int ans = base;
    while (p > 1) {
        ans *= base;
        --p;
    }
    return ans;
}

int main() {
    int n;
    scanf("%d", &n);
    int i;
    long long int ans = 0;
    for(i = 0; i < n; ++i) {
        int m;
        scanf("%d", &m);
        int base = m/10;
        int p = m % 10;
        ans += power(base, p);
    }
    printf("%lld\n", ans);
    return 0;
}
