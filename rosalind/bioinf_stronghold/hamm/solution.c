#include <stdio.h>
#include <string.h>

int main() {
    char a[2000], b[2000];
    scanf("%s", a);
    scanf("%s", b);
    int i;
    int n = strlen(a);
    int ans = 0;
    for (i = 0; i < n; ++i) {
        if (a[i] != b[i]) ++ans;
    }
    printf("%d\n", ans);
    return 0;
}
