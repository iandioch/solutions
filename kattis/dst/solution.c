#include <stdio.h>

int main() {
    int n;
    scanf("%d\n", &n);
    int ni;
    for (ni = 0; ni < n; ++ni) {
        char c;
        int change;
        int h, m;
        scanf("%c %d %d %d\n", &c, &change, &h, &m);
        int time = h*60 + m;
        if (c == 'B') change *= -1;
        time += change;
        while (time < 0) time += 24*60;
        while (time >= 24*60) time -= 24*60;
        printf("%d %d\n", time/60, time%60);
    }
    return 0;
}
