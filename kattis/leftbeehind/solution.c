#include <stdio.h>

int main() {
    while (1) {
        int sweet, sour;
        scanf("%d %d", &sweet, &sour);
        if (sweet == 0 && sour == 0) {
            break;
        }
        if (sweet + sour == 13) {
            printf("Never speak again.\n");
        } else if (sweet == sour) {
            printf("Undecided.\n");
        } else if (sweet > sour) {
            printf("To the convention.\n");
        } else {
            printf("Left beehind.\n");
        }
    }
    return 0;
}
