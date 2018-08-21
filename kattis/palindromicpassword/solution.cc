#include <cstdio>

#define li long int

int is_palindrome(li n) {
    if (n % 10 != ((n/100000))) return 0;
    if (((n/10)%10) != ((n/10000)%10)) return 0;
    return (((n/100)%10) == ((n/1000)%10));
}

int main() {
    li n, m, i, j;
    scanf("%ld", &n);
    for (i = 0; i < n; ++i) {
        scanf("%ld", &m);
        if (m == 100000) {
            printf("100001\n");
            continue;
        }
        if (is_palindrome(m)) {
            printf("%ld\n", m);
            continue;
        }
        for (j = 1; ; ++j) {
            if (is_palindrome(m-j)) {
                printf("%ld\n", m-j);
                break;
            } else if (is_palindrome(m+j)) {
                printf("%ld\n", m+j);
                break;
            }
        }
    }
    return 0;
}
