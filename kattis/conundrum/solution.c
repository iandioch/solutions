#include <stdio.h>
#include <string.h>

int main() {
    char c[305];
    scanf("%s", c);
    int n = strlen(c);
    int i;
    int ans = 0;
    for (i = 0; i < n; ++i) {
        if (i % 3 == 0 && c[i] != 'P') ++ans;
        if (i % 3 == 1 && c[i] != 'E') ++ans;
        if (i % 3 == 2 && c[i] != 'R') ++ans;
    }
    printf("%d\n", ans);
    return 0;
}
