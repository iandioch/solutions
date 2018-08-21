#include <cstdio>
#include <cstring>

using namespace std;

int fact[2];

inline int solve(long long int n) {
    // factorise
    int pos = 0;
    while (n%2 == 0) {
        fact[pos] += 1;
        n /= 2;
    }
    if (fact[pos]) ++pos;

    for (long long int i = 3; i*i <= n; i += 2) {
        while (n%i == 0) {
            if (pos > 1) return -1;
            ++fact[pos];
            n /= i;
        }
        if (fact[pos]) ++pos;
    }

    if (n > 1) {
        if (pos > 1) return -1;
        ++fact[pos];
        ++pos;
    }

    if (pos > 2) return -1;
    if (pos == 1) return fact[0]%2;
    if (fact[0] == fact[1]) return 0;
    if (fact[0] + 1 == fact[1] || fact[0] - 1 == fact[1]) {
        return 1;
    }
    return -1;
}

int main() {
    long long int n;
    scanf("%lld\n", &n);
    for (long long int i = 0; i < n; ++i) {
        long long int d;
        char s[10];
        scanf("%lld %s\n", &d, s);
        fact[0] = fact[1] = 0;
        int ans = solve(d);
        if (ans == 1) printf("%s\n", s);
        else if (ans == 0) printf("%s\n", s[0] == 'B' ? "Alice" : "Bob");
        else printf("tie\n");
    }
    return 0;
}
