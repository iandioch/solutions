#include <stdio.h>
#define LIM 101

int main() {
    while (1) {
        int n, k;
        scanf("%d", &n);
        if (n == 0) break;
        scanf("%d", &k);
        int w[LIM];
        int l[LIM];
        int i;
        for (i = 0; i < LIM; ++i) {
            w[i] = 0;
            l[i] = 0;
        }
        for (i = 0; i < k*n*(n-1)/2; ++i) {
            int a, b;
            char ac[10], bc[10];
            scanf("%d %s %d %s", &a, ac, &b, bc);
            --a;
            --b;
            if (ac[0] =='r') {
                if (bc[0] == 'p') {
                    ++w[b];
                    ++l[a];
                } else if (bc[0] == 's') {
                    ++w[a];
                    ++l[b];
                }
            } else if (ac[0] == 'p') {
                if (bc[0] == 's') {
                    ++w[b];
                    ++l[a];
                } else if (bc[0] == 'r') {
                    ++w[a];
                    ++l[b];
                }
            } else {
                if (bc[0] == 'r') {
                    ++w[b];
                    ++l[a];
                } else if (bc[0] == 'p') {
                    ++w[a];
                    ++l[b];
                }
            }
        }
        for (i = 0; i < n; ++i) {
            if (w[i] == 0 && l[i] == 0) {
                printf("-\n");
            } else {
                double f = ((double)w[i])/(w[i]+l[i]);
                printf("%.3f\n", f);
            }
        }
        printf("\n");
    }
    return 0;
}
