#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    char c[8];
    int curr = 0;
    int ok = 1;
    for (int i = 0; i < n; ++i) {
        ++curr;
        scanf("%s", c);
        if (c[0] == 'm') {
            continue;
        }
        int j = atoi(c);
        if (j != curr) {
            ok = 0;
            break;
        }
    }
    printf(ok?"makes sense\n":"something is fishy\n");
    return 0;
}
