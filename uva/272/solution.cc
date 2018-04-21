#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    bool in_quote = false;
    string s;
    while (getline(cin, s)) {
        string t = "";
        int j = 0;
        int len = s.size();
        for (j = 0; j < len; ++j) {
            if (s[j] == '\"') {
                if (in_quote) {
                    t += "''";
                } else {
                    t += "``";
                }
                in_quote = !in_quote;
            } else {
                t += s[j];
            }
        }
        cout << t << "\n";
    }
}
