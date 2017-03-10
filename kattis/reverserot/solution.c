#include <stdio.h>
#include <string.h>

int main() {
    char* s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.";
    int len = strlen(s);
    while (1) {
        int n;
        char c[50];
        scanf("%d ", &n);
        if (n == 0) break;
        scanf("%s", c);
        int i;
        for (i = strlen(c)-1; i >= 0; --i) {
            int j;
            switch(c[i]) {
                case '_':
                    j = 26;
                    break;
                case '.':
                    j = 27;
                    break;
                default:
                    j = c[i] - 'A';
            }
            j = (j+n) % 28;
            printf("%c", s[j]);
        }
        printf("\n");
    }
}
