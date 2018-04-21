#include <stdio.h>

int main() {
    long int a, b;
    while (scanf("%ld %ld", &a, &b) != EOF) {
        printf("%ld\n", 2*a*b);
    }
}
