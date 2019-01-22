#include <stdio.h>

int main() {
    char d[3];
    char a, b, c;
    int n;
    scanf("%s %d", d, &n);
    a = d[0];
    b = d[1];
    c = d[2];
    if ((a == 'D' && b == 'E' && c == 'C' && n == 25) ||
        (a == 'O' && b == 'C' && c == 'T' && n == 31)) {
        printf("yup\n");
        return 0;
    }
    printf("nope\n");
    return 0;
}
