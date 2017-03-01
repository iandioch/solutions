#include <stdio.h>

int main() {
    int n, p;
    scanf("%d %d", &n, &p);
    int i;
    char c[1000];
    for (i = 0; i < n; ++i) {
        scanf("%s", c);
    }
    printf("%d\n", p);
}
