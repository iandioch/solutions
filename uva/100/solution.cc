#include <stdio.h>
#define max(a, b) (a > b ? a : b)
#define min(a, b) (a > b ? b : a)

int main() {
    long int a, b;
    while (scanf("%ld %ld", &a, &b) != EOF) {
        long int start = min(a, b);
        long int end = max(a, b);
        long long int best = 0;
        for (long int i = start; i <= end; ++i) {
            long long int ans = 1;
            long int j = i;
            while (j != 1) {
                ++ans;
                if (j % 2 == 0) {
                    j /= 2;
                } else {
                    j = 3*j + 1;
                }
            }
            if (ans > best) best = ans;
        }
        printf("%ld %ld %lld\n", a, b, best);
    }
}
