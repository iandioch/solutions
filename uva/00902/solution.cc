#include <iostream>
#include <bits/stdc++.h>
#include <string>

using namespace std;

int main() {

    int n;
    string s;
    while (cin >> n >> s) {
        int maxn = -1;
        string best;
        map<string, int> q;
        int len = s.length();
        for (int i = 0; i + n <= len; ++i) {
            string substr = s.substr(i, n);
            ++q[substr];
            if (q[substr] > maxn) {
                best = substr;
                maxn = q[substr];
            }
        }
        cout << best << '\n';
    }
    return 0;
}
