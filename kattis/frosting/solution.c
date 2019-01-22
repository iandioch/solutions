#include <stdio.h>

int main() {
    long long int n;
    scanf("%lld\n", &n);
    int a[100001];
    int b[100001];
    long long int i, j;
    for (i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
    }

    long long int htot[3];
    htot[0] = 0;
    htot[1] = 0;
    htot[2] = 0;
    for (i = 0; i < n; ++i) {
        scanf("%d", &b[i]);

        htot[i%3] += b[i];
    }

    long long int tot[3];
    tot[0] = 0;
    tot[1] = 0;
    tot[2] = 0;
    int c;

    for (i = 0; i < n; ++i) {
        for(j = 0; j < 3; ++j) {
            tot[j] += htot[j]*a[i];
        }
        long long int tmp = htot[2];
        htot[2] = htot[1];
        htot[1] = htot[0];
        htot[0] = tmp;
    }
    printf("%lld %lld %lld\n", tot[1], tot[2], tot[0]);
    return 0;
}
