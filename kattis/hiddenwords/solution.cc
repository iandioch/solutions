#include <stdio.h>

#define MAX_DEPTH 10

using namespace std;

struct TrieNode {
    struct TrieNode *children[26];
    char c;
};

char grid[MAX_DEPTH][MAX_DEPTH];
bool visited[MAX_DEPTH][MAX_DEPTH];
int width, height;

void dfs(int x, int y, int depth, TrieNode *parent) {
    if (depth > MAX_DEPTH) return;
    if (visited[y][x]) return;
    visited[y][x] = 1;
    TrieNode *self = parent->children[grid[y][x]-'A'];
    if (!self) {
        self = new TrieNode();
        self->c = grid[y][x];
    }
    parent->children[grid[y][x]-'A'] = self;
    if (x < width - 1) dfs(x+1, y, depth+1, self);
    if (x > 0) dfs(x-1, y, depth+1, self);
    if (y < height - 1) dfs(x, y+1, depth+1, self);
    if (y > 0) dfs(x, y-1, depth+1, self);
    visited[y][x] = 0;
}

int main() {
    scanf("%d %d\n", &height, &width);
    for (int j = 0; j < height; ++j) {
        for (int i = 0; i < width; ++i) {
            scanf("%c", &grid[j][i]);
        }
        scanf("\n");
    }
    TrieNode *root = new TrieNode();
    root->c = '^';
    for (int j = 0; j < height; ++j) {
        for (int i = 0; i < width; ++i) {
            for (int p = 0; p < height; ++p) {
                for (int q = 0; q < width; ++ q) {
                    visited[p][q] = 0;
                }
            }
            dfs(i, j, 0, root);
        }
    }
    long long int num_word, ans = 0;
    scanf("%lld", &num_word);
    for (long long int i = 0; i < num_word; ++i) {
        char s[11];
        scanf("%s", s);
        TrieNode *pointer = root;
        for (int j = 0; j < 11; ++j) {
            if (s[j] == 0) {
                ++ans; //done
                break;
            }
            int ind = s[j] - 'A';
            if(pointer->children[ind]) {
                pointer = pointer->children[ind];
            } else {
                break;
            }
        }
    }
    printf("%lld\n", ans);
}
