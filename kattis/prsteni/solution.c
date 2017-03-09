#include <stdio.h>

int gcd(int a, int b) {
    if (a == b) return a;
    if (a > b) {
        return gcd(a-b, b);
    } else {
        return gcd(a, b-a);
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int d[105];
    int i;
    for (i = 0; i < n; ++i) {
        scanf("%d", &d[i]);
    }
    for (i = 1; i < n; ++i) {
        int a = d[0];
        int b = d[i];
        int c = gcd(a, b);
        a /= c;
        b /= c;
        printf("%d/%d\n", a, b);
    }
}
