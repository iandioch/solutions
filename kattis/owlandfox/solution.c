#include <stdio.h>

int digsum(long int n) {
    int ans = 0;
    while (n > 0) {
        ans += n % 10;
        n /= 10;
    }
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    int ti;
    for (ti = 0; ti < t; ++ti) {
        long int n;
        scanf("%ld", &n);
        long int i;
        int nsum = digsum(n) - 1;
        if (nsum == 0) {
            printf("0\n");
            continue;
        }
        for (i = n-1; i >= 0; --i) {
            if (digsum(i) == nsum) {
                printf("%ld\n", i);
                break;
            }
        }
    }
    return 0;
}
