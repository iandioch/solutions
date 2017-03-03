#include <stdio.h>
#include <string.h>

int main() {
    char a[2000], b[2000];
    scanf("%s", a);
    scanf("%s", b);
    int an = strlen(a);
    int bn = strlen(b);
    int i;

    char* ac = a;
    while (1) {
        char* d = strstr(ac, b);
        if (!d) {
            break;
        } else {
            printf("%ld ", d-a + 1);
            ac=d+1;
        }
    }
}
