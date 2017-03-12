#include <stdio.h>

int main() {
    int n, p, q;
    scanf("%d %d %d", &n, &p, &q);
    int t = p + q;
    if (t/n % 2 == 0) {
        printf("paul\n");
    } else {
        printf("opponent\n");
    }
    return 0;
}
