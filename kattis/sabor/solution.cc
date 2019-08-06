#include <cstdio>

#define MAXN 200001

using namespace std;

int args[MAXN][5]; // The IDs of the MPs they argued with.
int nargs[MAXN]; // The number of MPs they argued with.
bool party[MAXN]; // The party (0 or 1) of this MP.
int nopp[MAXN]; // The number of MPs they argued with of the same party.

void change(int i) {
    for (int j = 0; j < nargs[i]; ++j) {
        int opp = args[i][j];
        if(party[i] == party[opp]) {
            --nopp[i];
            --nopp[opp];
        } else {
            ++nopp[i];
            ++nopp[opp];
        }
    }
    party[i] = !party[i];
    for (int j = 0; j < nargs[i]; ++j) {
        int opp = args[i][j];
        if (nopp[opp] > 2) change(opp);
    }
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < 5; ++i) {
        int m;
        scanf("%d", &m);
        for (int j = 0; j < m; ++ j) {
            int a, b;
            scanf("  %d %d", &a, &b);
            --a;
            --b;
            args[a][nargs[a]] = b;
            args[b][nargs[b]] = a;
            nargs[a] += 1;
            nargs[b] += 1;
        }
    }

    for (int i = 0; i < n; ++i) {
        party[i] = true;
        nopp[i] = nargs[i];
    }

    for (int i = 0; i < n; ++i) {
        if (nopp[i] > 2) change(i);
    }

    for (int i = 0; i < n; ++i) {
        printf(party[i]? "A" : "B");
    }
    printf("\n");

    return 0;
}
