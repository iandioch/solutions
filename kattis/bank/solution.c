#include <stdio.h>
#define max(a,b) (a > b ? a : b)
#define min(a,b) (a > b ? b : a)

int main() {
    int num_ppl;
    int closing;
    scanf("%d %d", &num_ppl, &closing);
    int p;
    long long int amount[50];
    for (p = closing; p >= 0; --p) {
        amount[p] = 0;
    }
    for (p = 0; p < num_ppl; ++p) {
        long long int a;
        int t;
        scanf("%lld %d", &a, &t);
        int q;
        for (q = t; a > 0 && q >= 0; --q) {
            long long int b = amount[q];
            amount[q] = max(a, b);
            a = min(a, b);
        }
    }
    long long int ans = 0;
    for (p = 0; p < closing; ++p) {
        ans += amount[p];
    }
    printf("%lld\n", ans);
    return 0;
}
