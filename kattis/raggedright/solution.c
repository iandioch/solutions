#include <stdio.h>
#include <string.h>

int main() {
    int len[101];
    int i = 0;
    int max = 0;
    while (1) {
        char c[100];
        fgets(c, 100, stdin);
        if (feof(stdin)) {
            break;
        }
        len[i] = strlen(c);
        if (len[i] > max) {
            max = len[i];
        }
        ++i;
    }
    long long int ans = 0;
    --i;
    --i;
    while (i >= 0) {
        ans += (max - len[i])*(max - len[i]);
        --i;
    }
    printf("%lld\n", ans);
    return 0;
}
