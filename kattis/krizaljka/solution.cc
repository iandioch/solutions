#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

string a, b;

int main() {
    cin >> a >> b;
    for (int i = 0; i < a.size(); ++i) {
        char c = a[i];
        int j = b.find(c);
        if (j != string::npos) {
            // I got them backwards, so swap them.
            string d = a;
            a = b;
            b = d;
            for (int y = 0; y < a.size(); ++y) {
                if (y == j) {
                    cout << b << "\n";
                    continue;
                }
                for (int x = 0; x < i; ++x) {
                    printf(".");
                }
                printf("%c", a[y]);
                for (int x = i + 1; x < b.size(); ++x) {
                    printf(".");
                }
                printf("\n");
            }
            return 0;
        }
    }
    return 0;
}
