#include <stdio.h>
#include <bitset>

using namespace std;

bitset<100000001> composite;

int main() {
    long long int n;
    long long int q;
    scanf("%lld %lld", &n, &q);
    ++n;
    composite[1] = 1;
    long long int iter;
    long long int i, j, k;

    long long int numprime = 0;
    
    if (n > 2) {
        numprime += 1;
    }

    for (i = 3; i < n; i+=2) {
        if (!composite[i]) {
            ++numprime;
            for (j = i*3; j < n; j += i+i) {
                composite[j] = 1;
            }
        }
    }
    long long int c;

    printf("%lld\n", numprime);
    for (iter = 0; iter < q; ++iter) {
        scanf("%lld", &c);
        if (c % 2) printf("%d\n", (!composite[c]));
        else if (c == 2) printf("1\n");
        else printf("0\n");
    }
    return 0;
}
