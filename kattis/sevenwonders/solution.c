#include <stdio.h>
#include <string.h>

int main() {
    int c[3];
    c[0] = 0;
    c[1] = 0;
    c[2] = 0;
    char s[100];
    scanf("%s", s);
    int i;
    for (i = 0; i < strlen(s); ++i) {
        if (s[i] == 'T') {
            ++c[0];
        } else if (s[i] == 'C') {
            ++c[1];
        } else {
            ++c[2];
        }
    }
    long int ans = 0;
    unsigned int n = -1;
    for (i = 0; i < 3; ++i) {
        if (c[i] < n) {
            n = c[i];
        }
        ans += c[i]*c[i];
    }
    printf("%ld\n", ans + n*7);
}
