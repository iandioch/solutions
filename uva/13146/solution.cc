#define min(a, b) ((a) < (b) ? (a) (b))
#include <iostream>

using namespace std;

int levenshtein(string a, string b) {
    int d[105][105];
    int m = a.length();
    int n = b.length();
    for (int i = 1; i <= m; ++i) {
        d[i][0] = i;
    }
    for (int j = 1; j <= n; ++j) {
        d[0][j] = j;
    }
    for (int j = 1; j <= n; ++j) {
        for (int i = 1; i <= m; ++i) {
            int cost = 0;
            if (a[i-1] != b[j-1]) {
                cost = 1;
            }
            d[i][j] = min(d[i-1][j] + 1,
                      min(d[i][j-1] + 1,
                          d[i-1][j-1] + cost));
        }
    }
    return d[m][n];
}

int main() {
    int n;
    cin >> n;
    cin.ignore();
    while (n--) {
        string a, b;
        getline(cin, a);
        getline(cin, b);
        cout << levenshtein(a, b) << "\n";
    }
    return 0;
}
