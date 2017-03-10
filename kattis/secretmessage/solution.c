#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    char c[500][500];
    int ntests;
    scanf("%d", &ntests);
    int test;
    for (test = 0; test < ntests; ++test) {
        char s[10005];
        scanf("%s", s);
        int n = strlen(s);
        int m = (int) sqrt(n + 0.0);
        if (m*m < n) ++m;
        int i;
        int x = 0, y = 0;
        for (i = 0; i < n; ++i) {
            x = i % m;
            y = i/m;
            c[x][y] = s[i];
        }
        for (i = n; i < m*m; ++i) {
            x = i % m;
            y = i/m;
            c[x][y] = '*';
        }
        for (x = 0; x < m; ++x) {
            for (y = m-1; y >= 0; --y) {
                if (c[x][y] == '*') {
                    continue;
                }
                printf("%c", c[x][y]);
            }
        }
        printf("\n");
    }
    return 0;
}
