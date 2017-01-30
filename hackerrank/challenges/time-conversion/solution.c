#include <stdio.h>

int main() {
    int h, m, s;
    char am[2];
    scanf("%d:%d:%d%s", &h, &m, &s, am);

    if (h == 12) {
        if (am[0] == 'A') {
            printf("00:");
        } else {
            printf("12:");
        }
    } else {
        if (am[0] == 'A') {
            if (h < 10) printf("0");
            printf("%d:", h);
        } else {
            printf("%d:", h+12);
        }
    }
    if (m < 10) printf("0");
    printf("%d:", m);
    if (s < 10) printf("0");
    printf("%d", s);
}
