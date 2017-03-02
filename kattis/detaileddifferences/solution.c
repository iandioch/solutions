#include <stdio.h>
#include <string.h>

int main() {
    char a[100];
    char b[100];
    int num_tests;
    scanf("%d", &num_tests);
    int test;
    for (test = 0; test < num_tests; ++test) {
        scanf("%s", a);
        scanf("%s", b);
        int i;
        printf("%s\n%s\n", a, b);
        for (i = 0; i < strlen(a); ++i) {
            if (a[i] == b[i]) printf(".");
            else printf("*");
        }
        printf("\n\n");
    }
    return 0;
}
