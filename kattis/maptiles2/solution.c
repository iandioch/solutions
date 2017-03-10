#include <stdio.h>
#include <string.h>

long long int intpow(int base, int p) {
    long long int a = 1;
    int i;
    for (i = 0; i < p; ++i) {
        a *= base;
    }
    return a;
}

int main() {
    char s[32];
    scanf("%s", s);
    int n = strlen(s);
    int i;
    long long int x = 0, y = 0;
    for (i = 0; i < n; ++i) {
        long long int z = intpow(2, n-i-1);
        if (s[i] == '1') {
            x += z;
        } else if (s[i] == '2') {
            y += z;
        } else if (s[i] == '3') {
            x += z;
            y += z;
        }
    }
    printf("%d %lld %lld\n", n, x, y);
    return 0;
}
