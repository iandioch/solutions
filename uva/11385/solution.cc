#include <iostream>
#include <cstdio>

using namespace std;

long long int fib[1000];

void calcFib() {
    long long int a = 1;
    long long int b = 1;
    int curr = 0;
    while (b < 2147483648) {
        fib[curr] = b;
        long int c = a + b;
        a = b;
        b = c;
        ++curr;
    }
}

void op() {
    int n;
    long long int f[101];
    string s;

    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%lld", &f[i]);
    }
    scanf("\n");
    getline(cin, s);

    char a[102];
    for (int i = 0; i < 102; ++i) {
        a[i] = ' ';
    }
    int pt = -1;
    int maxn = 0;
    for (int i = 0; i < n; ++i) {
        do {
            ++pt;
            if (pt >= s.length()) pt = 0;
            //pt %= s.length();
        } while (s[pt] < 'A' || s[pt] > 'Z');
        int fi = 0;
        while (fib[fi] != f[i]) {
            ++fi;
        }
        a[fi] = s[pt];
        if (fi > maxn) maxn = fi;
    }
    a[maxn+1] = 0;
    printf("%s\n", a);
}

int main() {
    calcFib();
    int n;
    scanf("%d\n", &n);
    while (n--) {
        op();
    }
}
