#include <stdio.h>

int main() {
    int e, f, cost;
    scanf("%d %d %d", &e, &f, &cost);
    int empty = e + f;
    int ans = 0;
    while (empty >= cost) {
        empty -= cost;
        ++ans;
        ++empty;
    }
    printf("%d\n", ans);
}
