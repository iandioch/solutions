#include <stdio.h>
#include <string.h>

int main() {
    char c[251];
    scanf("%s", c);
    int len = strlen(c);
    printf("%c", c[0]);
    int i;
    for (i = 1; i < len; ++i) {
        if (c[i] != c[i-1]) printf("%c", c[i]);
    }
    printf("\n");
}
