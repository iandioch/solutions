#include <stdio.h>

int main() {
    int d;
    scanf("%d", &d);
    printf("%ssatisfactory\n", d < 8 ? "un" : "");
}
