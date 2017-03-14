#include <stdio.h>

int main() {
    int ntests;
    scanf("%d", &ntests);
    int test;
    for (test = 1; test <= ntests; ++test) {
        long long int k, p, q;
        scanf("%lld %lld/%lld", &k, &p, &q);
        if (p == q) {
            printf("%d %lld/%lld\n", test, p, q+1);
        } else if (p < q) {
            printf("%d %lld/%lld\n", test, q, q-p);
        } else {
            if (q == 1) {
                // if the denominator is 1, know the next is 1/(numerator+1)
                printf("%d 1/%lld\n", test, p+1);
                continue;
            }
            long long int x = 0;
            while (p > q) {
                /* traverse the tree upwards until we find the node we
                   should take the other branch at */
                p -= q;
                ++x;
            }
            // find its parent
            q -= p;
            // go to the other branch
            p += q;
            // keep going down the left hand side
            q += p*x;
            printf("%d %lld/%lld\n", test, p, q);
        }
    }
    return 0;
}
