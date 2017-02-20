#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int i;
    for (i = 0; i < n; ++i) {
        int j = 0;
        for (j = 0; j < (n-i)-1; ++j) {
            printf(" ");
        } 
        for (; j < n; ++j) {
            printf("#");
        }
        printf("\n");
    }
    return 0;
}
