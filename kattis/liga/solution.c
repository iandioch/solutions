#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define UNKNOWN -1234

int read_int() {
    char c[10];
    scanf("%s", c);
    if (c[0] == '?') {
        return UNKNOWN;
    }
    return atoi(c);
}

int main() {
    int tests;
    scanf("%d", &tests);
    int t;
    for (t = 0; t < tests; ++t) {
        int a, b, c, d, e;
        a = read_int();
        b = read_int();
        c = read_int();
        d = read_int();
        e = read_int();

        int bmax, bmin;
        int cmax, cmin;
        if (b == UNKNOWN) {
            bmax = 100;
            bmin = 0;
        } else {
            bmax = b;
            bmin = b;
        }

        if (c == UNKNOWN) {
            cmax = 100;
            cmin = 0;
        } else {
            cmax = c;
            cmin = c;
        }

        if (a == UNKNOWN && d == UNKNOWN) {
            // Only one case where this is possible.
            d = 0;
        }

        int bi, ci;
        for (bi = bmin; bi <= bmax; ++bi) {
            for (ci = cmin; ci <= cmax; ++ci) {
                int ai = (a == UNKNOWN ? bi + ci + d : a);
                int di = (d == UNKNOWN ? ai - bi - ci : d);
                int ei = (e == UNKNOWN ? 3*bi + ci : e);

                if (ai == bi + ci + di && ai >= 0 && ai <= 100 && di >= 0 && di <= 100 && ei == 3*bi + ci) {
                    printf("%d %d %d %d %d\n", ai, bi, ci, di, ei);
                }
            }
        }
    }
    return 0;
}
