#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    int ti;
    for (ti = 0; ti < t; ++ti) {
        int n, m;
        scanf("%d %d\n", &n, &m);
        int x[105];
        int i;
        for (i = 0; i < m; ++i) {
            x[i] = 0;
        }
        for (i = 0; i < n; ++i) {
            int j;
            for (j = 0; j < m; ++j) {
                char c;
                scanf("%c", &c);
                if (c == '0') {
                    --x[j];
                } else {
                    ++x[j];
                }
            }
            scanf("\n");
        }
        for (i = 0; i < m; ++i) {
            if (x[i] >= 0) {
                printf("1");
            } else {
                printf("0");
            }
        }
        printf("\n");
    }
}
