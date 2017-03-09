#include <stdio.h>

int main() {
    int r, c;
    scanf("%d %d", &r, &c);
    printf("%lf\n", 100*((c-r)*(c-r) + 0.0)/(r*r));
}
