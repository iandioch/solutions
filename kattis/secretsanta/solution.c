#include <stdio.h>

int main() {
    long long int n;
    scanf("%lld", &n);
    // our answer is 1 - (!n)/(n!)
    // !n is the number of derangements of n
    // n! is n factorial

    // seeing as !n = (n!) (sigma i->n) ((-1)**(i)/(i!)),
    // we can factor out the n! from numerator and denominator.
    // answer is then = 1 - (sigma i->n) ((-1)**(i)/(i!))


    // this is 1/e, which the answer converges to very quickly;
    // !n = round(n!/e), so (!n)/(n!) = round(n!/e)/(n!), which
    // is very close to 1/e
    long double ans = 0.367879441171442;

    if (n < 50) {

        long long int f = 1;
        long long int i;
        // ans starts at 1 to account for starting at i = 1, 
        // instead of i = 0
        ans = 1;
        for (i = 1; i <= n; ++i) {
            if (i % 100000 == 0) printf("%lld\n", i);
            f *= i;
            if (i % 2 == 0) {
                ans += 1.0/f;
            } else {
                ans -= 1.0/f;
            }
        }
    }
    printf("%.8Lf\n", 1-ans);
    return 0;
}
