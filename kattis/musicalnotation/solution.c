#include <stdio.h>
#define NUMLETTERS 14

char stave[255][200];
char pad[255];
char letters[NUMLETTERS] = "GFEDCBAgfedcba";

int main() {
    pad['G'] = ' ';
    pad['F'] = '-';
    pad['E'] = ' ';
    pad['D'] = '-';
    pad['C'] = ' ';
    pad['B'] = '-';
    pad['A'] = ' ';
    pad['g'] = '-';
    pad['f'] = ' ';
    pad['e'] = '-';
    pad['d'] = ' ';
    pad['c'] = ' ';
    pad['b'] = ' ';
    pad['a'] = '-';
    int n;
    scanf("%d\n", &n);
    int i, j, k;
    char c, d;
    int curr = 0;
    for (i = 0; i < n; ++i) {
        scanf("%c", &c);
        scanf("%c", &d);
        int repeats = 0;
        while (d != ' ' && d != '\n') {
            repeats *= 10;
            repeats += (d-'0');
            scanf("%c", &d);
        }
        if (repeats == 0) ++repeats;
        for (j = curr; j < curr + repeats; ++j) {
            stave[c][j] = '*';
            for (k = 0; k < NUMLETTERS; ++k) {
                if (letters[k] == c) continue;
                stave[letters[k]][j] = pad[letters[k]];
            }
        }
        curr += repeats;
        if (d != ' ') {
            scanf(" ");
            stave[c][curr] = '*';
            for (j = 0; j < NUMLETTERS; ++j) {
                if (letters[j] == c) continue;
                stave[letters[j]][curr] = pad[letters[j]];
            }
            ++curr;
        }
        for (j = 0; j < NUMLETTERS; ++j) {
            stave[letters[j]][curr] = pad[letters[j]];
        }
        ++curr;
    }
    for (i = 0; i < NUMLETTERS; ++i) {
        printf("%c: ", letters[i]);
        for (j = 0; j < curr-2; ++j) {
            printf("%c", stave[letters[i]][j]);
        }
        printf("\n");
    }
    return 0;
}
