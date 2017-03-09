#include <stdio.h>
#include <string.h>

int main() {
    char c[101];
    fgets(c, 101, stdin);
    
    int i = 0;
    int n = strlen(c);
    for (i = 0; i < n; ++i) {
        printf("%c", c[i]);
        if (c[i] == 'a' ||
            c[i] == 'e' ||
            c[i] == 'i' ||
            c[i] == 'o' ||
            c[i] == 'u') {
            i += 2;
        }
    }
    return 0;
}
