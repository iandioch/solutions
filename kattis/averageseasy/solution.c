#include <stdio.h>
#define STUDENTS 200001

int main() {
    int num_tests;
    scanf("%d\n", &num_tests);
    int test;
    long long int cs[STUDENTS];
    long long int eco[STUDENTS];
    for (test = 0; test < num_tests; ++test) {
        long long int n_cs = 0;
        long long int n_eco = 0;
        scanf("\n%lld %lld\n", &n_cs, &n_eco);
        long long int i;
        long long int tot_cs = 0;
        long long int tot_eco = 0;
        for (i = 0; i < n_cs; ++i) {
            scanf("%lld", &cs[i]);
            tot_cs += cs[i];
        }
        scanf("\n");
        for (i = 0; i < n_eco; ++i) {
            scanf("%lld", &eco[i]);
            tot_eco += eco[i];
        }
        long long int ans = 0;
        long double mean_cs = (0.0+tot_cs)/n_cs;
        long long mean_eco = (0.0+tot_eco)/n_eco;
        for (i = 0; i < n_cs; ++i) {
            if (cs[i] < mean_cs && cs[i] > mean_eco) {
                ++ans;
            }
        }
        printf("%lld\n", ans);
    }
}
