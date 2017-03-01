#include <stdio.h>

int digsum(int n) {
    int ans = 0;
    while (n > 0) {
        ans += n%10;
        n /= 10;
    }
    return ans;
}

int main() {
    int l, d, x;
    scanf("%d %d %d", &l, &d, &x);
    int i;
    for (i = l; i <= d; ++i) {
        int s = digsum(i);
        if (s == x) {
            printf("%d\n", i);
            break;
        }
    }
    for (i = d; i >= l; --i) {
        int s = digsum(i);
        if (s == x) {
            printf("%d\n", i);
            break;
        }
    }
}
