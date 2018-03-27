#include <stdio.h>

#define max(a, b) (a > b ? a : b)

int n;
double prob[22][22];
int done[1<<22];
double memo[1<<22];

/*
 * curr = The Bond currently being placed.
 * missions = bitmask of already assigned missions
 */
double solve(int curr, int missions) {
    if (curr == n) return 1.0;
    if (done[missions]) return memo[missions];
    done[missions] = 1;
    double ans = 0.0;
    int i;
    for (i = 0; i < n; ++i) {
        if ((missions & (1 << i)) == 0) {
            double d = prob[curr][i] * solve(curr+1, missions | (1<<i));
            ans = max(ans, d);
        }
    }
    memo[missions] = ans;
    return ans;
}

int main() {
    scanf("%d", &n);
    int i, j;
    for (i = 0; i < n; ++i) {
        for (j = 0; j < n; ++j) {
            int percent;
            scanf("%d", &percent);
            prob[i][j] = percent / 100.0;
        }
    }
    double ans = solve(0, 0);
    printf("%.6f\n", ans * 100);
    return 0;
}
