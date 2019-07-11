#include <stdio.h>
#include <unordered_set>

using namespace std;

unordered_set<int> instrument[1001];
bool avail[1001];

int main() {
    int ninstr, nnote;
    scanf("%d %d", &ninstr, &nnote);
    for (int i = 0; i < ninstr; ++i) {
        avail[i] = 1;
        int k;
        scanf("%d", &k);
        for (int j = 0; j < k; ++j) {
            int l;
            scanf("%d", &l);
            instrument[i].insert(l);
        }
    }
    int ans = 0;
    for (int i = 0; i < nnote; ++i) {
        int note;
        scanf("%d", &note);
        int navail = 0;
        //printf("note = %d\n", note);
        for (int j = 0; j < ninstr; ++j) {
            if (instrument[j].find(note) == instrument[j].end()) avail[j] = 0;
            if (!avail[j]) continue;
            ++navail;
            //printf("%d is available.\n", j);
        }
        if (navail == 0) {
            ++ans;
            //printf("switch @ %d\n", i);
            for (int j = 0; j < ninstr; ++j) {
                if (instrument[j].find(note) != instrument[j].end()) avail[j] = 1;
            }
        }
    }
    printf("%d\n", ans);
}
