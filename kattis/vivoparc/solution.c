#include <stdio.h>

int n;
int adj[101][101];
int colour[101];

int try_combo() {
    int curr = -1;
    int i = -1;
    for (i = 0; i < n; ++i) {
        if (colour[i] == -1) {
            curr = i;
            break;
        }
    }
    if (curr == -1) {
        return 1;
    }
    //printf("curr = %d\n", curr);

    int col;
    for (col = 1; col <= 4; ++col) {
        int other;
        int ok = 1;
        for (other = 0; other < n; ++other) {
            if (adj[curr][other] && colour[other] == col) {
                ok = 0;
                break;
            }
        }
        if (!ok) {
            continue;
        }
        colour[curr] = col;
        if(try_combo()) {
            return 1;
        }
        colour[curr] = -1;
    }
    return 0;
}

int main() {
    scanf("%d\n", &n);
    int i;
    for (i = 0; i < n; ++i) {
        int j;
        for (j = 0; j < n; ++j) {
            adj[i][j] = 0;
        }
    }

    int a, b;
    while (scanf("%d-%d\n", &a, &b) != EOF) {
        --a;
        --b;
        adj[a][b] = 1;
        adj[b][a] = 1;
    }

    //printf("done inputs\n");

    for (i = 0; i < n; ++i) {
        colour[i] = -1;
    }
    colour[0] = 1;
    try_combo();
    for (i = 0; i < n; ++i) {
        printf("%d %d\n", i+1, colour[i]);
    }

    return 0;
}
