#include <stdio.h>

int main() {
    int best = 0;
    short besti = -1;
    short i;
    for (i = 1; i < 6; ++i) {
        int a, b, c, d;
        scanf("%d %d %d %d", &a, &b, &c, &d);
        if (a+b+c+d > best) {
            best = a+b+c+d;
            besti = i;
        }
    }
    printf("%hd %d", besti, best);
}
