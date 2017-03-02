#include <stdio.h>

int main() {
    double cost;
    int lawns;
    scanf("%lf", &cost);
    scanf("%d", &lawns);
    int lawn;
    double area = 0;
    for (lawn = 0; lawn < lawns; ++lawn) {
        double w, h;
        scanf("%lf %lf", &w, &h);
        area += w*h;
    }
    printf("%.8lf\n", area*cost);
}
