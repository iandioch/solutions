#include <stdio.h>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    map<string, int> m;
    int n;
    scanf("%d\n", &n);
    for (int i = 0; i < n; ++i) {
        string s;
        getline(cin, s);
        auto it = m.find(s);
        if (it != m.end()) {
            m[s] = m[s] + 1;
        } else {
            m[s] = 1;
        }
    }

    int min = 10000;
    for (auto const& x: m) {
        if (x.second < min) min = x.second;
    }

    vector<string> o;
    for (auto const& x: m) {
        if (x.second == min) {
            o.push_back(x.first);
        }
    }

    sort(o.begin(), o.end());

    for (auto const& x: o) {
        cout << x << "\n";
    }

    return 0;
}
