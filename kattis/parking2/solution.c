#include <stdio.h>

int main() {
    int num_tests;
    scanf("%d", &num_tests);
    int t;
    for (t = 0; t < num_tests; ++t) {
        int n;
        scanf("%d", &n);
        unsigned int min = -1;
        int max = 0;
        int i;
        for (i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            if (x < min) {
                min = x;
            }
            if (x > max) {
                max = x;
            }
        }
        printf("%d\n", 2*(max-min));
    }
    return 0;
}
