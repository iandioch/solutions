#include <stdio.h>

int main() {
    int d[9];
    int i;
    int tot = 0;
    for (i = 0; i < 9; ++i) {
        scanf("%d", &d[i]);
        tot += d[i];
    }
    int j, k;
    for (i = 0; i < 8; ++i) {
        for (j = i+1; j < 9; ++j) {
            if (i == j) {
                continue;
            }
            if (tot - d[i] - d[j] == 100) {
                for (k = 0; k < 9; ++k) {
                    if (k == i || k == j) {
                        continue;
                    }
                    printf("%d\n", d[k]);
                }
                return 0;
            }
        }
    }
    return 0;
}
