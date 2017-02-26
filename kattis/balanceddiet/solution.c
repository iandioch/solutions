#include <stdio.h>
#define M 126000

long int m[21];
int poss[M];

int main() {
    while (1) {
        int n;
        scanf("%d", &n);
        if (n == 0) break;

        if (n == 1) {
            // edge case: only 1 can
            int g;
            scanf("%d", &g);
            printf("%d 0\n", g);
            continue;
        }

        // clear out prev test case
        int i, j;
        for (i = 0; i < M; ++i) {
            poss[i] = 0;
        }

        // max sum is ~12600
        long int sum = 0;
        for (i = 0; i < n; ++i) {
            scanf("%ld", &m[i]);
            sum += m[i];

            for (j = sum+10; j >= 0; --j) {
                poss[j+m[i]] |= poss[j];
            }
            poss[m[i]] = 1;
        }

        long int besta;
        unsigned long int bestdiff = -1;

        for (i = 0; i < sum; ++i) {
            if (poss[i]) {
                // a > b, a + b = sum
                long int a, b;
                if (sum-i-i < 0) {
                    a = i;
                    b = sum-i;
                } else {
                    a = sum-i;
                    b = i;
                }
                if (a-b < bestdiff) {
                    besta = a;
                    bestdiff = a-b;
                }
            }
        }

        if (besta > sum-besta) {
            printf("%ld %ld\n", besta, sum-besta);
        } else {
            printf("%ld %ld\n", sum-besta, besta);
        }
    }
    return 0;
}
