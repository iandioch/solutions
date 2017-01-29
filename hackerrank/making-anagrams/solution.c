#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char a[10005], b[10005];
    scanf("%s", a);
    scanf("%s", b);
    int count[26];
    int i;
    for (i = 0; i < 26; ++i) {
        count[i] = 0;
    }

    for (i = 0; i < strlen(a); ++i) {
        ++count[a[i] - 'a'];
    }
    for (i = 0; i < strlen(b); ++i) {
        --count[b[i] - 'a'];
    }

    int ans = 0;
    for (i = 0; i < 26; ++i) {
        ans += abs(count[i]);
    }
    printf("%d\n", ans);

    return 0;
}
