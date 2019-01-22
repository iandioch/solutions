#include <stdio.h>

int main() {
    long int n;
    scanf("%ld", &n);
    long long int m[100001];
    long long int min = 1000000000;
    for (long int i = 0; i < n; ++i) {
        scanf("%lld", &m[i]);
        if (m[i] < min) min = m[i];
    }
    for (long int i = 0; i < n; ++i) {
        if (m[i] == min) {
            printf("%ld\n", i);
            break;
        }
    }
    return 0;
}
