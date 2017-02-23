#include <stdio.h>
#include <stdlib.h>

int compare (const void * a, const void * b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int n[3];
    scanf("%d %d %d", &n[0], &n[1], &n[2]);
    qsort(n, 3, sizeof(int), compare);
    char c[5];
    scanf("%s", c);
    int i;
    for (i = 0; i < 3; ++i) {
        printf("%d ", n[c[i]-'A']);
    }
    printf("\n");
}
