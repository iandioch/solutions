#include <stdio.h>

int main() {
    int k;
    int n;
    scanf("%d\n%d", &k, &n);
    --k;
    int i;
    int time = 0;
    for (i = 0; i < n; ++i) {
        int t;
        char c;
        scanf("%d %c", &t, &c);
        time += t;
        if (time > 210){
            break;
        }
        if (c == 'T') {
            k = (k+1)%8;
        }
    }
    printf("%d\n", k+1);
    return 0;
}
