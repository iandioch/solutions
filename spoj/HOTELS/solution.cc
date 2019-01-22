#include <cstdio>

#define ll long long int
#define MAXN 300001

using namespace std;

long long int n, m;

long long int cost[MAXN];

int main() {
    scanf("%lld %lld", &n, &m);
    for (ll i = 0; i < n; ++i) {
        scanf("%lld", &cost[i]);
    }

    ll i = 0;
    ll j = 0;
    ll tot = cost[0];
    ll best = 0;
    while (j <= n) {
        if (tot > m) {
            tot -= cost[i];
            ++i;
        } else {
            best = (best > tot ? best : tot);
            if (j < n- 1) {
                ++j;
                tot += cost[j];
            } else {
                break;
            }
        }
    }
    printf("%lld\n", best);
    return 0;
}
