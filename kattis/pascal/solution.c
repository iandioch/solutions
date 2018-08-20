#include <stdio.h>

int main() {
    long long int n;
    long long int i;
    scanf("%lld", &n);
    if (n == 1) {
        printf("0\n");
        return 0;
    } else {
        if (n % 2 == 0) {
            printf("%lld\n", n-(n/2));
            return 0;
        }
        for (i = 3; i*i <= n; i += 2) {
            if (n % i == 0) {
                printf("%lld\n", n - (n/i));
                return 0;
            }
        }
    }
    printf("%lld\n", n-1);
    return 0;
}
