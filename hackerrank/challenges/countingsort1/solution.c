#include <stdio.h>

int main() {
    long int count[100];
    int i;
    for (i = 0; i < 100; ++i) {
        count[i] = 0;
    }
    int n;
    scanf("%d", &n);
    for (i = 0; i < n; ++i) {
        int m;
        scanf("%d", &m);
        ++count[m];
    }
    for (i = 0; i < 100; ++i) {
        printf("%ld ", count[i]);
    }
}
