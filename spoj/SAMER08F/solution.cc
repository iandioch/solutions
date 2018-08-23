#include <cstdio>

using namespace std;

int main() {
    while (1) {
        long long int n;
        scanf("%lld", &n);
        if (n == 0) break;
        printf("%lld\n", (n*(n+1)*(2*n + 1))/6);
    }
    return 0;
}
