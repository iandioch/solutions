#include <stdio.h>
#include <string.h>

int main() {
    char s[51];
    scanf("%s", s);
    int n = strlen(s);
    short a = 1, b = 0, c = 0;
    int i;
    short t;
    for (i = 0; i < n; ++i) {
        if (s[i] == 'A') {
            t = a;
            a = b;
            b = t;
        } else if (s[i] == 'B') {
            t = b;
            b = c;
            c = t;
        } else {
            t = a;
            a = c;
            c = t;
        }
    }
    if (a == 1) printf("1\n");
    if (b == 1) printf("2\n");
    if (c == 1) printf("3\n");
    return 0;
}
