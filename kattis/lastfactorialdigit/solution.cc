#include <stdio.h>

int main() {
    int last[11];
    last[1] = 1;
    for (int i = 2; i < 11; ++i) {
        last[i] = (last[i-1]*i)%10;
    }
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        int m;
        scanf("%d", &m);
        printf("%d\n", last[m]);
    }
    return 0;
}
