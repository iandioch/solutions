#include <math.h>
#include <stdio.h>
#define degreesToRadians(a) ((a) * M_PI / 180.0)

double lat[1000], lng[1000];
double degLat[1000], degLng[1000];

double dist(double lat1, double lng1, double lat2, double lng2) {
    double dLat = lat2 - lat1;
    double dLng = lng2 - lng1;
    double a = sin(dLat/2.0)*sin(dLat/2.0) + cos(lat1)*cos(lat2)*sin(dLng/2.0)*sin(dLng/2.0);
    return 2.0*asin(a);
}

int main() {
    while (!feof(stdin)) {
        int n;
        scanf("%d\n", &n);
        int i;
        double best = -1;
        int bestI = 0;
        for (i = 0; i < n; ++i) {
            scanf("%lf %lf\n", &degLat[i], &degLng[i]);
            lat[i] = degreesToRadians(degLat[i]);
            lng[i] = degreesToRadians(degLng[i]);
        }
        for (i = 0; i < n; ++i) {
            int j;
            double maxD = -1;
            for (j = 0; j < n; ++j) {
                if (i == j) continue;
                double d = dist(lat[i], lng[i], lat[j], lng[j]);
                if (d > maxD) maxD = d;
            }
            if (maxD <= best || best < 0) {
                best = maxD;
                bestI = i;
            }
        }
        printf("%.2lf %.2lf\n", degLat[bestI], degLng[bestI]);

    }
}
