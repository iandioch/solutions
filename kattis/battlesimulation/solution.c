#include <stdio.h>
#include <string.h>

int main() {
    char c[1000005];
    scanf("%s", c);
    int n = strlen(c);
    int i;
    for (i = 0; i < n; ++i) {
        if (i + 2 < n) {
            int hasR = 0;
            int hasB = 0;
            int hasL = 0;
            int j;
            for (j = 0; j < 3; ++j) {
                if (c[i+j] == 'R') ++hasR;
                else if (c[i+j] == 'B') ++hasB;
                else if (c[i+j] == 'L') ++hasL;
            }
            if (hasR == 1 && hasB == 1 && hasL == 1) {
                printf("C");
                i += 2;
                continue;
            }
        }
        switch (c[i]) {
            case 'R':
                printf("S");
                break;
            case 'B':
                printf("K");
                break;
            case 'L':
                printf("H");
        }
    }
    printf("\n");
    return 0;
}
