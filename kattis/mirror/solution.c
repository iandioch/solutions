#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);
    char c[50][50];
    int h, w;
    int ti;
    for (ti = 0; ti < t; ++ti) {
        scanf("%d %d\n", &h, &w);
        int y;
        for (y = 0; y < h; ++y) {
            fgets(c[y], 50, stdin);
        }
        printf("Test %d\n", ti+1);
        for (y = h-1; y >= 0; --y) {
            int x;
            for (x = w-1; x >= 0; --x) {
                printf("%c", c[y][x]);
            }
            printf("\n");
        }
    }
    return 0;
}
