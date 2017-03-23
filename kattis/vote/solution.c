#include <stdio.h>

int main() {
    unsigned long long int first;
    unsigned long long int second;
    unsigned long long int curr;
    unsigned long long int tot;
    int besti;
    int numtests;
    int test;
    int numcandidates;
    int currcand;
    scanf("%d", &numtests);
    for (test = 0; test < numtests; ++test) {
        first = 0;
        second = 0;
        besti = 0;
        tot = 0;
        scanf("%d", &numcandidates);
        for (currcand = 0; currcand < numcandidates; ++currcand) {
            scanf("%llu", &curr);
            tot += curr;
            if (curr > first) {
                second = first;
                first = curr;
                besti = currcand + 1;
            } else if (curr > second) {
                second = curr;
            }
        }
        if (first == second) {
            printf("no winner\n");
        } else {
            if (tot - first < first) {
                printf("majority");
            } else {
                printf("minority");
            }
            printf(" winner %d\n", besti);
        }
    }
    return 0;
}
