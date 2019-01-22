#include <stdio.h>
#include <string.h>

char s[75];
int len;

int cmp(int a, int b, int size) {
    int i;
    for (i = 0; i < size; ++i) {
        if (b+i >= len) continue;
        if (s[a+i] == s[b+i]) continue;
        else return 0;
    }
    return 1;
}

int possible(int m) {
    int done = m;
    while (done < len) {
        if(!cmp(0, done, m)) return 0;
        done += m;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d\n", &n);
    int i;
    for (i = 0; i < n; ++i) {
        fgets(s, 75, stdin);
        len = strlen(s) - 1;

        int m;
        int ok = 0;
        for (m = 1; m < len; ++m) {
            if (possible(m)) {
                printf("%d\n", m);
                ok = 1;
                break;
            }
        }
        if (!ok) printf("%d\n", len);
    }
}
