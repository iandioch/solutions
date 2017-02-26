#include <stdio.h>
#define abs(a) ((a)>0?(-a):(a))

int main() {
    int start;
    int desired;
    scanf("%d\n%d", &start, &desired);
    int ans = ((360-start) + desired);
    while (ans > 180) ans -= 360;
    printf("%d\n", ans);
}
