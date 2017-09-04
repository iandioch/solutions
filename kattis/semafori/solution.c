#include <stdio.h>

int main() {
    long int dist = 0, time = 0;
    long int d, r, g;
    long int numlights, totdist;
    scanf("%ld %ld", &numlights, &totdist);
    long int i;
    long int lastd = 0;
    for (i = 0; i < numlights; ++i) {
        scanf("%ld %ld %ld", &d, &r, &g);
        dist += d-lastd;
        time += d-lastd;
        long int cycles = time/(r+g);
        long int ready = cycles*(r+g) + r;
        while (time < ready) {
            ++time;
        }
        lastd = d;
    }
    time += totdist - lastd;
    printf("%ld\n", time);
}
