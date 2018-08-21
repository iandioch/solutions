#include <algorithm>
#include <cstdio>

#define ll long long int
#define MAXN 200001

using namespace std;

ll ntasks, ntimes;

ll tasks[MAXN];
ll times[MAXN];

int main() {
    scanf("%lld %lld", &ntasks, &ntimes);
    ll i, j;
    for (i = 0; i < ntasks; ++i) {
        scanf("%lld", &tasks[i]);
    }
    for (i = 0; i < ntimes; ++i) {
        scanf("%lld", &times[i]);
    }

    sort(tasks, tasks + ntasks);
    sort(times, times + ntimes);

    ll ans = 0;
    i = ntasks - 1;
    j = ntimes - 1;
    while (i >= 0 && j >= 0) {
        if (tasks[i] <= times[j]) {
            ++ans;
            --i;
            --j;
        } else {
            --i;
        }
    }
    printf("%lld\n", ans);
    return 0;
}
