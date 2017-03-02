#include <stdio.h>

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n < 0) break;

        int i;
        long int ans = 0;
        int p = 0;
        for (i = 0; i < n; ++i) {
            int s, t;
            scanf("%d %d", &s, &t);
            ans += s*(t-p);
            p = t;
        }
        printf("%ld miles\n", ans);
    }
    return 0;
}
