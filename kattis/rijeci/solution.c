#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    long long int a = 1, b = 0;
    while (n > 0) {
        long long int na = b;
        long long int nb = a+b;
        a = na;
        b = nb;
        --n;
    }
    printf("%lld %lld\n", a, b);
}
