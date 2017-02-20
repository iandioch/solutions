#include <stdio.h>

int main(){
    int n; 
    scanf("%d",&n);
    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          scanf("%d",&a[a_i][a_j]);
       }
    }

    int i;
    long int diff = 0;
    for (i = 0; i < n; ++i) {
        diff += a[i][i];
    }
    for (i = 0; i < n; ++i) {
        diff -= a[n-i-1][i];
    }
    if (diff < 0) diff *= -1;
    printf("%ld\n", diff);

    return 0;
}
