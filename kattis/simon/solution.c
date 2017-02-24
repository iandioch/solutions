#include <stdio.h>
#include <string.h>

int main() {
    char* simon = "simon says";
    int n;
    scanf("%d\n", &n);
    int i;
    for (i = 0; i < n; ++i) {
        char c[1001];
        fgets(c, 1001, stdin);
        if (strstr(c, simon) == c) {
            printf("%s\n", &c[11]);
        } else {
            printf("\n");
        }
    }
}
