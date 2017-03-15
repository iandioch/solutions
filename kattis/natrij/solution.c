#include <stdio.h>

long int countsecs(int h, int m, int s){
    return h*60*60 + m*60 + s;
}

int main() {
    int h, m, s;
    scanf("%d:%d:%d", &h, &m, &s);
    int hi, mi, si;
    scanf("%d:%d:%d", &hi, &mi, &si);
    long int a = countsecs(h, m, s);
    long int b = countsecs(hi, mi, si);
    if (a >= b) {
        b += 24*60*60;
    }
    long int c = b-a;
    int ha = 0;
    while (c >= 60*60) {
        ++ha;
        c -= 60*60;
    }
    int ma = 0;
    while (c >= 60) {
        ++ma;
        c -= 60;
    }
    printf("%02d:%02d:%02ld\n", ha, ma, c);
    return 0;
}
