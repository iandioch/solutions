#include <iostream>
#include <cmath>

using namespace std;

int main() {

    double d;
    cin >> d;

    double ans = (d*1000*5280.0)/4854.0;

    cout << (long long int) (ans+0.5) << "\n";

    return 0;
}
