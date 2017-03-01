#include <stdio.h>

int main() {
    long long int n;
    scanf("%lld", &n);
    if (n % 2 == 0) {
        printf("Bob\n");
    } else {
        printf("Alice\n");
    }
    return 0;
}
