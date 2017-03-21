#include <stdio.h>

int main() {
    while (1) {
        long int n, d;
        int p;
        scanf("%ld %ld %d", &n, &d, &p);
        if (feof(stdin)) {
            break;
        }
        int count;
        printf("0.");
        for (count = 0; count < p; ++count) {
            n *= 10;
            printf("%ld", n/d);
            n %= d;
        }
        printf("\n");
    }
    return 0;
}
