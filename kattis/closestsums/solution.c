#include <stdio.h>
#define diff(x, y) (x < y ? (y-x) : (x-y))
#define abs(x) (x < 0 ? (-x) : x)

long int m[1001];
long int o[5000000];

int main() {
    int test_case = 0;
    while (1) {
        ++test_case;
        int n;
        scanf("%d", &n);
        if (feof(stdin)) break;
        int i;
        for (i = 0; i < n; ++i) {
            scanf("%ld", &m[i]);
        }
        int j;
        int num_combo = 0;
        for (i = 0; i < n; ++i) {
            for (j = i+1; j < n; ++j) {
                o[num_combo] = m[i] + m[j];
                ++num_combo;
            }
        }
        int g;
        scanf("%d", &g);
        printf("Case %d:\n", test_case);
        for (i = 0; i < g; ++i) {
            long int best = -1;
            unsigned long int best_diff = -1;
            long int target;
            scanf("%ld", &target);
            for (j = 0; j < num_combo; ++j) {
                if (diff(target, o[j]) <= best_diff) {
                    best_diff = diff(target, o[j]);
                    best = o[j];
                }
            }
            printf("Closest sum to %ld is %ld.\n", target, best);
        }
    }
    return 0;
}
