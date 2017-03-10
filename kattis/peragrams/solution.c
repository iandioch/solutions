#include <stdio.h>
#include <string.h>

int main() {
    int count[26];
    int i;
    for (i = 0; i < 26; ++i) {
        count[i] = 0;
    }
    char s[1001];
    scanf("%s", s);
    int len = strlen(s);
    for (i = 0; i < len; ++i) {
        ++count[s[i]-'a'];
    }
    int numodd = 0;
    for (i = 0; i < 26; ++i) {
        if (count[i] % 2 != 0) {
            ++numodd;
        }
    }
    if (numodd == 0) {
        printf("0\n");
    } else {
        printf("%d\n", numodd-1);
    }
    return 0;
}
