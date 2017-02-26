#include <stdio.h>
#define max(a, b) (a > b ? a : b)
#define min(a, b) (a < b ? a : b)

int main() {
    int num_tests;
    scanf("%d", &num_tests);
    int test;
    for (test = 0; test < num_tests; ++test) {
        int pole_len, num_ants;
        scanf("%d %d", &pole_len, &num_ants);
        int shortest = 0;
        int longest = 0;
        int i;
        for (i = 0; i < num_ants; ++i) {
            int a;
            scanf("%d", &a);
            shortest = max(shortest, min(a, pole_len-a));
            longest = max(longest, max(a, pole_len-a));
        }
        printf("%d %d\n", shortest, longest);
    }
}
