#include <stdio.h>
#include <math.h>

int main() {
    int n;
    scanf("%d", &n);
    int i;
    for (i = 0; i < n; ++i) {
        int m;
        scanf("%d", &m);
        printf("%d\n", (int) ceil(m/400.0));
    }
    return 0;
}
