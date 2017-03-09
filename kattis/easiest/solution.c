#include <stdio.h>

int sum_digs(long long int n) {
    int a = 0;
    while (n > 0) {
        a += n % 10;
        n /= 10;
    }
    return a;
}

int main() {
    while (1) {
        long long int n;
        scanf("%lld", &n);
        if (n == 0) break;
        long long int p;
        long long int s = sum_digs(n);
        for (p = 11; sum_digs(n*p) != s; ++p) {}
        printf("%lld\n", p);
    }
    return 0;
}
