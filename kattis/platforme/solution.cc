#include <stdio.h>
#include <algorithm>

using namespace std;

struct platform {
    long long int left, right, y;
};

int compare_platform(platform a, platform b) {
    return (a.y < b.y);
}

platform p[102];
int top[10001];

int main() {
   int n;
   scanf("%d", &n);
   for (int i = 0; i < n; ++i) {
       scanf("%lld %lld %lld", &p[i].y, &p[i].left, &p[i].right);
       --p[i].right;
   }
   sort(p, p+n, compare_platform);
   long long int ans = 0;
   for (int i = 0; i < n; ++i) {
        ans += 2*p[i].y - top[p[i].left] - top[p[i].right];
        for (long long int j = p[i].left; j <= p[i].right; ++j) {
            top[j] = p[i].y;
        }
   }
   printf("%lld\n", ans);
  
}
