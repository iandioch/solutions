#include <stdio.h>
#include <string.h>
#define MAX 102

#define max(a, b) (a > b ? a : b)

int main() {
    int a[MAX], b[MAX];

    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));
    int a_tmp[MAX], b_tmp[MAX];

    int n;
    scanf("%d", &n);
    int ni;
    for (ni = 0; ni < n; ++ni) {
        int ai, bi;
        scanf("%d %d", &ai, &bi);

        ++a[ai];
        ++b[bi];

        int i;
        for (i = 0; i < MAX; ++i) {
            a_tmp[i] = a[i];
            b_tmp[i] = b[i];
        }

        int ans = 0;

        int curr_a = MAX-1;
        int curr_b = 1;

        while(curr_a > 0 && curr_b < MAX) {
            while (curr_a > 0 && !a_tmp[curr_a]) --curr_a;
            while (curr_b < MAX && !b_tmp[curr_b]) ++curr_b;

            if (curr_a == 0 || curr_b == MAX) {
                // No more nums.
                break;
            }

            ans = max(ans, curr_a+curr_b);

            if (a_tmp[curr_a] > b_tmp[curr_b]) {
                a_tmp[curr_a] -= b_tmp[curr_b];
                b_tmp[curr_b] = 0;
            } else {
                b_tmp[curr_b] -= a_tmp[curr_a];
                a_tmp[curr_a] = 0;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
