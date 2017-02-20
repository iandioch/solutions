#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_pal(int n) {
    char c[10];
    sprintf(c, "%d", n);
    int i;
    int j = strlen(c);
    for (i = 0; i < j/2; ++i) {
        if (c[i] != c[j-i-1]) return 0;
    }
    return 1;
}

int main() {
    int is_pal_prod[1000000];
    memset(is_pal_prod, 0, sizeof(is_pal_prod));
    int i, j, r;
    for (i = 0; i < 1000; ++i) {
        for (j = i; j < 1000; ++j) {
            r = i*j;
            if (is_pal(r) > 0) {
                is_pal_prod[r] = 1;
            }
        }
    }
    int nt;
    scanf("%d", &nt);
    int t;
    for (t = 0; t < nt; ++t) {
        int n;
        scanf("%d", &n);
        --n;
        while (n > 0 && (is_pal_prod[n] == 0)) --n;
        printf("%d\n", n);
    }
}
