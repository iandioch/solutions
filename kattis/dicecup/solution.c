#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    if (b < a) {
        int c = a;
        a = b;
        b = c;
    }
    int i;
    for (i = a+1; i < b+2; ++i) {
        printf("%d\n", i);
    }
}
