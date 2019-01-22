#include <stdio.h>

using namespace std;

int main() {
    int n;
    int m[1000001];

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &m[i]);
    }

    int ans = 0;
    int done = 0;
    while (done < n) {
        for (int i = 0; i < n; ++i) {
            if (m[i] > 0) {
                ++ans;
                int h = m[i];
                for (int j = i; j < n; ++j) {
                    if (h <= 0) break;
                    if (m[j] == h) {
                        m[j] = 0;
                        --h;
                        ++done;
                    }
                }
            }
        }
    }
    printf("%d\n", ans);
}
