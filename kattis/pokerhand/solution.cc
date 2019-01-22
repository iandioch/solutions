#include <iostream>
#include <map>

using namespace std;

int main() {
    map<char, int> m;

    for (int i = 0; i < 5; ++i) {
        char a[2];
        cin >> a;
        ++m[a[0]];
    }

    int max = 0;
    for (auto const &x: m) {
        if (x.second > max) max = x.second;
    }
    cout << max << "\n";
    return 0;
}
