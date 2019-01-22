#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int n;
    cin >> n;
    unordered_set<int> m;
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        for (int j = a; j <= b; ++j) {
            m.emplace(j);
        }
    }

    cout << m.size() << "\n";
    return 0;
}
