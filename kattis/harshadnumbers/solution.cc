#include <iostream>

using namespace std;

bool is_harshad(long long int n) {
    long long int digsum = 0;
    long long int m = n;
    while (m) {
        digsum += m%10;
        m/=10;
    }
    return !(n % digsum);
}

int main() {
    long long int n;
    cin >> n;
    while (!is_harshad(n)) ++n;
    cout << n << "\n";
    return 0;
}
