#include <stdio.h>

int main() {
    int score;
    int a, b, c, i, j, k;

    char *s[3] = {"single", "double", "triple"};
    scanf("%d", &score);
    for (a = 20; a >= 1; --a) {
        for (b = 20; b >= 1; --b) {
            for (c = 20; c >= 1; --c) {
                for (i = 3; i >= 1; --i) {
                    for (j = 3; j >= 0; --j) {
                        for (k = 3; k >= 0; --k) {
                            if (a*i + b*j + c*k == score) {
                                printf("%s %d\n", s[i-1], a);
                                if(j > 0) printf("%s %d\n", s[j-1], b);
                                if(k > 0) printf("%s %d\n", s[k-1], c);
                                return 0;
                            }
                        }
                    }
                }
            }
        }
    }
    printf("impossible\n");
    return 0;
}
