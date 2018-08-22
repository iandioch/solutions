#include <cstdio>

#define MAXN 100

long long int sour[MAXN];
long long int bitter[MAXN];

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%lld %lld", &sour[i], &bitter[i]);
    }
    long long int bestdiff = 1000000000;
    for (int i = 1; i < (1<<(n)); ++i) {
        //printf("test %d\n", i);
        long long int s = 1, b = 0;
        for (int j = 0; j < n; ++j) {
            if ((1<<j) & i) {
                //printf(" - inc %d\n", j);
                s *= sour[j];
                b += bitter[j];
            }
        }
        //printf("%lld %lld\n", s, b);
        long long int d = (s > b ? s-b : b-s);
        if (d < bestdiff) bestdiff = d;
    }
    printf("%lld\n", bestdiff);
    return 0;
}
