#include <cstdio>
#include <cstring>

using namespace std;

#define ll long long int

ll n;

ll reverse(ll in) {
    ll r = 0;
    while (in > 0) {
            r *= 10;
            r += (in % 10);
            in /= 10;
    }
    return r;

}

int main() {
    scanf("%lld", &n);
    for (ll i = 0; i < n; ++i) {
        ll p, q;
        scanf("%lld %lld", &p, &q);
        printf("%lld\n", reverse(reverse(p) + reverse(q)));
    }
    return 0;
}
