#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    // ans = n choose 4, as for any set of 4 vertices
    // there is one unique intersection of diagonals
    // nCr(n, r) = (n!)/((r!) * ((n-k)!))
    // nC4 = n! / (4! * (n-4)!)
    // However, (n!)/((n-4)!) = n*(n-1)*(n-2)*(n-3),
    // and 4! = 24. Therefore:
    long int ans = n*(n-1)*(n-2)*(n-3)/24;
    printf("%ld\n", ans);
}
