#include <stdio.h>

int main() {
    int x, n;
    scanf("%d\n%d\n", &x, &n);
    long int g = x;
    int i, j;
    for (i = 0; i < n; ++i) {
        scanf("%d", &j);
        g += x;
        g -= j;
    }
    printf("%ld\n", g);
    return 0;
}
