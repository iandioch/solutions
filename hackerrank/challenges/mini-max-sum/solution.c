#include <stdio.h>

int main() {
    long long a[5];
    scanf("%lld %lld %lld %lld %lld", &a[0], &a[1], &a[2], &a[3], &a[4]);
    
    long long tot = 0;
    long long max = 0;
    long long min = 1000000000;
    int i;
    for (i = 0; i < 5; ++i) {
        tot += a[i];
        if (a[i] > max) max = a[i];
        if (a[i] < min) min = a[i];
    }
    printf("%lld %lld", tot-max, tot-min);
}
