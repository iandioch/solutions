#include <stdio.h>
#include <string.h>

int main() {
    char a;
    char s[200];
    scanf("%c %s", &a, s);
    int n = strlen(s);
    if (a == 'E') {
        char curr = s[0];
        int m = 1;
        int i;
        for (i = 1; i < n; ++i) {
            fflush(stdout);
            if (s[i] == curr) {
                ++m;
            } else {
                printf("%c%d", curr, m);
                m = 1;
                curr = s[i];
            }
        }
        printf("%c%d\n", curr, m);
        fflush(stdout);
    } else {
        for (int i = 0; i < n; i += 2) {
            for (int j = 0; j < (s[i+1]-'0'); ++j) {
                printf("%c", s[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
