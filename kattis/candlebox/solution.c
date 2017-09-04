#include <stdio.h>
#define rsum(n) ((n)*(n+1)/2)
#define rsum2(n) (n)*(n+1)

int main() {
    long long int d, r, t;
    scanf("%lld\n%lld%lld", &d, &r, &t);
    long long int k;
    long long int a = 0, b = 0;
    for (k = 4; ; ++k) {
        a += k;
        if (k - d >= 3) {
            b += k - d;
        }
        if (a+b == r+t) {
            printf("%lld\n", r-a);
            break;
        }
    }
    return 0;
}
