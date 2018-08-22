#include <cstdio>

#define MAXN 101
#define MAXM 101

long long int time;

int n, m;
long long int a[MAXN], b[MAXN], c[MAXM], d[MAXM];

long long int found(long long int test) {
    long long int tot = 0;
    for (int i = 0; i < n; ++i) {
        long long int t = test - a[i];
        if (t < 0) continue;
        tot += (t/b[i]) + 1;
    }
    return tot;
}

long long int cracked(long long int test) {
    long long int tot = 0;
    for (int i = 0; i < m; ++i) {
        long long int t = test - c[i];
        if (t < 0) continue;
        tot += (t/d[i]) + 1;
    }
    return tot;
}

long long int binsearch(long long int lo, long long int hi) {
    while (hi - lo > 1) {
        long long int mid = (lo+hi)/2;
        long long int x = found(mid);
        long long int y = cracked(time-mid);
        if (x > y) hi = mid;
        else lo = mid;
    }
    return lo;
}

int main() {
    scanf("%lld", &time);

    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%lld %lld", &a[i], &b[i]);
    }
    scanf("%d", &m);
    for (int i = 0; i < m; ++i) {
        scanf("%lld %lld", &c[i], &d[i]);
    }
    printf("%lld\n", binsearch(1, time));
    return 0;
}
