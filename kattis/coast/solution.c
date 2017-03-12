#include <stdio.h>

char c[1005][1005];
int seen[1005][1005];
int w, h;
int i, j, k;

void floodfill(int x, int y, char n, char orig) {
    if (x < 0 || x > w + 1 || y < 0 || y > h + 1) {
        return;
    }
    if (seen[y][x] > 0) {
        return;
    }
    seen[y][x] = 1;
    if (c[y][x] == orig) {
        c[y][x] = n;
        floodfill(x+1, y, n, orig);
        floodfill(x-1, y, n, orig);
        floodfill(x, y+1, n, orig);
        floodfill(x, y-1, n, orig);
    }
}

int main() {
    scanf("%d %d\n", &h, &w);
    for (i = 0; i < w+2; ++i) {
        c[0][i] = '0';
        c[h+1][i] = '0';
    }
    for (i = 0; i < h+2; ++i) {
        c[i][0] = '0';
        c[i][w+1] = '0';
    }
    for (i = 1; i <= h; ++i) {
        for (j = 1; j <= w; ++j) {
            char d;
            scanf("%c", &c[i][j]);
        }
        c[i][w+3] = '\0';
        scanf("%c", ((char*) &k));
    }
    for (i = 0; i < h+2; ++i) {
        for (j = 0; j < w+2; ++j) {
            seen[i][j] = 0;
        }
    }
    floodfill(0, 0, '.', '0');
    long int ans = 0;
    for (i = 1; i < h+1; ++i) {
        for (j = 1; j < w+1; ++j) {
            if (c[i][j] == '1') {
                if (c[i-1][j] == '.') ++ans;
                if (c[i+1][j] == '.') ++ans;
                if (c[i][j-1] == '.') ++ans;
                if (c[i][j+1] == '.') ++ans;
            }
        }
    }
    printf("%ld\n", ans);
}
