#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d\n", &n);
    int i;
    for (i = 0; i < n; ++i) {
        char c = ' ';
        long int m = 0;
        while (1) {
            scanf("%c", &c);
            if (c == '\n') {
                break;
            }
            ++m;
        }
        printf("%ld\n", m);
    }
}
