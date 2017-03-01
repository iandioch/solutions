#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int i;
    for (i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        if (x % 2 == 0) {
            printf("%d is even\n", x);
        } else {
            printf("%d is odd\n", x);
        }
    }
}
