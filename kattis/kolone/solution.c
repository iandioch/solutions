#include <stdio.h>

int main() {
    int n1, n2;
    char c1[26], c2[26];
    scanf("%d %d", &n1, &n2);
    scanf("%s %s", c1, c2);
    int moving_left[26];
    int i;
    for (i = 0; i < 26; ++i) {
        moving_left[i] = 0;
    }
    for (i = 0; i < n2; ++i) {
        moving_left[c2[i]-'A'] = 1;
    }

    char c[30];
    for (i = 0; i < n1; ++i) {
        c[i] = c1[n1-i-1];
    }
    for (i = 0; i < n2; ++i) {
        c[n1+i] = c2[i];
    }
    c[n1+n2] = '\0';

    int n;
    scanf("%d", &n);
    int m;
    for (m = 0; m < n; ++m) {
        for (i = 0; i < n1+n2-1; ++i) {
            if (moving_left[c[i]-'A'] < moving_left[c[i+1]-'A']) {
                char tmp = c[i];
                c[i] = c[i+1];
                c[i+1] = tmp;
                i += 1;
            }
        }
    }
    printf("%s\n", c);
    return 0;
}
