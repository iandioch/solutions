#include <stdio.h>
#include <unordered_map>

using namespace std;

int main() {
    long long int m;
    scanf("%lld", &m);

    unordered_map<long long int, long long int> s;

    long long int max = 0;
    for (long long int i = 1; ; ++i) {
        long long int p = i*i*i;

        for (long long int j = i; ; ++j) {
            long long int q = j*j*j;
            long long int a = p+q;
            if (a > m) break;
            ++ s[a];
            if (s[a] >= 2 && a > max) max = a;
        }
        if (p > m) break;
    }

    if (max == 0) {
        printf("none\n");
    } else {
        printf("%lld\n", max);
    }

    return 0;
}
