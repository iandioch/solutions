#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int n, k, w;
char c[101];
char ticker[101];

int overlap() {
    for(int kk = k; kk > 0; --kk) {
        bool ok = true;
        for (int ci = 0; ci < kk; ++ci) {
            int tk = ci + (k-kk);
            if (ticker[tk] != c[ci]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return kk;
        }
    }
    return 0;
}

int main() {
    scanf("%d", &n);
    for (int ni = 0; ni < n; ++ni) {
        scanf("%d %d", &k, &w);
        for (int i = 0; i < k; ++i) {
            ticker[i] = ' ';
        }
        ticker[k] = 0;
        int ans = 0;
        for (int wi = 0; wi < w; ++wi) {
            scanf("%s", c);
            //printf("ticker: %s\n", ticker);
            //printf("input: %s\n", c);
            //printf("overlap: %d\n", overlap());
            ans += k - overlap();
            strcpy(ticker, c);
        }
        printf("%d\n", ans);
    }
    return 0;
}
