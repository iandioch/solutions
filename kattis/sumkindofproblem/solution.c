#include <stdio.h>
#define LIM 10000*2+1

int main() {
    long long int first[LIM], odd[LIM], even[LIM];
    int i;
    int f = 0, o = 0, e = 0;
    first[0] = odd[0] = even[0] = 0;
    for (i = 1; i < LIM; ++i) {
        first[i] = first[i-1] + i;
        odd[i] = odd[i-1];
        even[i] = even[i-1];
        if (i % 2 == 0) {
            even[i] += i;
        } else {
            odd[i] += i;
        }
    }
    int num;
    scanf("%d", &num);
    for (i = 0; i < num; ++i) {
        int k, n;
        scanf("%d %d", &k, &n);
        printf("%d %lld %lld %lld\n", k, first[n], odd[n*2], even[n*2]);
    }
}
