#include <stdio.h>
#include <bitset>

#define MAXN 50000

using namespace std;

bitset<MAXN> composite;

int is_prime(long long int n) {
    if (n == 2 || n == 3) return 1;
    if (n % 2 == 0) return 0;
    if (n % 3 == 0) return 0;
    if (n < MAXN) {
        return (!composite[n]);
    }
    long long int w = 2;
    long long int i = 5;
    while (i*i <= n) {
        if (n % i == 0) return 0;
        i += w;
        w = 6 - w;
    }
    return 1;
}

int main() {
    composite[1] = 1;
    long long int i, j;

    for (i = 3; i < MAXN; i+=2) {
        if (!composite[i]) {
            for (j = i*3; j < MAXN; j += i+i) {
                composite[j] = 1;
            }
        }
    }
    long long int c;


    while (1) {
        scanf("%lld", &c);
        switch (c) {
            case 0:
                return 0;
            case 2:
                printf("5\n");
                break;
            default:
                int prime = 1;
                if (c % 2 == 0) {
                    prime = 0;
                } else if (c < MAXN) {
                    prime = !composite[c];
                } else {
                    prime = is_prime(c);
                }
                long long int nextPrime = c*2 + 1;
                while (!is_prime(nextPrime)){
                    ++nextPrime;
                }
                if (prime) {
                    printf("%lld\n", nextPrime);
                } else {
                    printf("%lld (%lld is not prime)\n", nextPrime, c);
                }
        }
    }
    return 0;
}
