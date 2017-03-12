#include <stdio.h>

int main() {
    int c[4];
    c[0] = 0;
    scanf("%d %d %d", &c[1], &c[2], &c[3]);
    int arrive[3];
    int depart[3];
    int i;
    for (i = 0; i < 3; ++i) {
        scanf("%d %d", &arrive[i], &depart[i]);
    }
    int ans = 0;
    for (i = 1; i <= 100; ++i) {
        int n = 0;
        int j;
        for (j = 0; j < 3; ++j) {
            if (i >= arrive[j] && i < depart[j]) {
                ++n;
            }
        }
        ans += c[n]*n;
    }
    printf("%d\n", ans);
    return 0;
}
