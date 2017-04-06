#include <stdio.h>
#include <string.h>

char *target = "welcome to code jam";
char in[505];
int d[505][505];
int n, m, p, i, j, k, g, h;
int inl, targetl;

int main() {
    targetl = strlen(target);
    scanf("%d\n", &n);
    for (i = 1; i <= n; ++i) {
        fgets(in, 505, stdin);
        inl = strlen(in);
        for (k = 0; k < targetl; ++k) {
            d[0][k] = 0;
        }
        for (j = 0; j < inl; ++j) {
            for (k = 0; k < targetl; ++k) {
                if (j > 0) {
                    d[j][k] = d[j-1][k];
                } else {
                    d[j][k] = 0;
                }
                if (in[j] == target[k]) {
                    // add one above to it
                    if (k > 0) {
                        d[j][k] += d[j][k-1];
                    } else {
                        ++d[j][k];
                    }
                }
                d[j][k] %= 10000;
            }
        }
        printf("Case #%d: %.4d\n", i, d[inl-1][targetl-1]);
    }
    return 0;
}
