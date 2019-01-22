#include <cstdio>

#define ll long long int

using namespace std;

long long int n[1000002];

int main() {
    n[0] = 2;
    for (ll i = 1; i <= 1000000; ++i) {
        n[i] = (n[i-1] + i + (i+1)*2)%1000007;
    }
    ll t;
    scanf("%lld", &t);
    while (t--) {
        ll p;
        scanf("%lld", &p);
        printf("%lld\n", n[p-1]);
    }
    return 0;
}
