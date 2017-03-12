#include <stdio.h>
#include <string.h>
#include <math.h>

int main() {
    int t, ti;
    scanf("%d\n", &t);
    char d[105][105];
    char c[10005];
    for (ti = 0; ti < t; ++ti) {
        int i, j;
        fgets(c, 10005, stdin);
        int n = (int) sqrt(strlen(c));
        int k = 0;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                d[i][j] = c[k];
                ++k;
            }
        }
        for (i = n-1; i >= 0; --i) {
            for (j = 0; j < n; ++j) {
                printf("%c", d[j][i]);
            }
        }
        printf("\n");
    }
    return 0;
}
