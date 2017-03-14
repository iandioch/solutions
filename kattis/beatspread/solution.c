#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    int ti;
    for (ti = 0; ti < t; ++ti) {
        int sum, diff;
        scanf("%d %d", &sum, &diff);
        int a, b;
        int found = 0;
        for (a = sum; a >= 0; --a) {
            b = a-diff;
            if (a + b == sum) {
                printf("%d %d\n", a, b);
                found = 1;
                break;
            }
        }
        if (found == 0) {
            printf("impossible\n");
        }
    }
    return 0;
}
