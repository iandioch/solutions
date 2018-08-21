#include <cstdio>

#define MAXN 1001

#define max(a, b) ((a) < (b) ? (b) : (a))

long long int t[MAXN][MAXN];
long long int a[MAXN][MAXN];
int h, w;

int main() {
    scanf("%d %d", &h, &w);
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            scanf("%lld", &t[i][j]);
        }
    }
    a[0][0] = t[0][0];
    for(int i = 1; i < w; ++i) {
        a[0][i] = a[0][i-1] + t[0][i];
    }
    for (int i = 1; i < h; ++i) {
        a[i][0] = a[i-1][0] + t[i][0];
        for (int j = 1; j < w; ++j) {
            a[i][j] = t[i][j] + max(a[i-1][j], a[i][j-1]);
        }
    }
    for (int i = 0; i < h; ++i) {
        printf("%lld ", a[i][w-1]);
    }
    printf("\n");
    return 0;
}
