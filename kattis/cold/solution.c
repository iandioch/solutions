#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int i;
    int ans = 0;
    for (i = 0; i < n; ++i) {
        long int m;
        scanf("%ld", &m);
        if (m < 0) ++ans;
    }
    printf("%d\n", ans);
}
