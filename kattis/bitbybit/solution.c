#include <stdio.h>

int main() {
    char c[32];
    while (1) {
        int i, j, k;
        for (i = 0; i < 32; ++i) {
            c[i] = '?';
        }
        int n;
        scanf("%d", &n);
        if (n == 0) {
            break;
        }
        for (i = 0; i < n; ++i) {
            char instruction[8];
            scanf("%s", instruction);
            if (instruction[0] == 'S') {
                // SET
                scanf("%d", &j);
                c[j] = '1';
            } else if (instruction[0] == 'C') {
                //CLEAR
                scanf("%d", &j);
                c[j] = '0';
            } else if (instruction[0] == 'O') {
                //OR
                scanf("%d %d", &j, &k);
                if (c[k] == '1' || c[j] == '1') {
                    c[j] = '1';
                } else if (c[k] == '?') {
                    c[j] = '?';
                }
            } else {
                //AND
                scanf("%d %d", &j, &k);
                if (c[k] == '0' || c[j] == '0') {
                    c[j] = '0';
                } else if (c[k] == '?') {
                    c[j] = '?';
                }
            }
        }
        for (i = 31; i >= 0; --i) {
            printf("%c", c[i]);
        }
        printf("\n");
    }
    return 0;
}
