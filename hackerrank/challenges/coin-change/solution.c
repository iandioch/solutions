#include <stdio.h>

int main() {
    int desired, numCoins;
    scanf("%d %d", &desired, &numCoins);
    int c[51];
    int i;
    for (i = 0; i < numCoins; ++i) {
        scanf("%d", &c[i]);
    }
    long long n[251];
    for (i = 0; i < 251; ++i) {
        n[i] = 0;
    }
    n[0] = 1;
    int j;
    for (j = 0; j < numCoins; ++j) {
        for (i = 0; i < desired + 1; ++i) {
            int k = i - c[j];
            if (k < 0) continue;
            n[i] += n[k];
        }
    }

    printf("%lld\n", n[desired]);
}
