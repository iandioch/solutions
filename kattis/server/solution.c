#include <stdio.h>

int main() {
    int n, t;
    scanf("%d %d", &n, &t);
    int i;
    int ans = 0;
    for (i = 0; i < n; ++i) {
        int m;
        scanf("%d", &m);
        if (t >= m) {
            t -= m;
        } else {
            break;
        }
        ++ans;
    }
    printf("%d\n", ans);
    return 0;
}
