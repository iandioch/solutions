#include <iostream>

using namespace std;

long long int ssd(long int base, long int n) {
    long long int ans = 0;
    while (n) {
        int d = (n%base);
        ans += d*d;
        n /= base;
    }
    return ans;
}

int main() {
    int n;
    cin >> n;
    for (int nn = 0; nn < n; ++nn) {
        long int dnum, base, n;
        cin >> dnum >> base >> n;


        long long int ans = ssd(base, n);
        cout << dnum << " " << ans << "\n";
    }
    return 0;
}
