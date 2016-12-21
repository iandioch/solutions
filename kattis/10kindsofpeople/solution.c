#include <stdio.h>
#define LIM 200000

int g[1001][1001];
int c[1001][1001];
int w, h;

void colour (int x, int y, long int col, int orig) {
	// out of bounds
	if (x < 0 || y < 0 || x >= w || y >= h) return;
	// not right 0 or 1
	if (g[x][y] != orig) return; 
	// already been here
	if (c[x][y] == col) return;

	c[x][y] = col;

	colour(x+1, y, col, orig);
	colour(x-1, y, col, orig);
	colour(x, y+1, col, orig);
	colour(x, y-1, col, orig);
}

int main() {
	scanf("%d %d", &h, &w);
	int i, j;
	for (i = 0; i < h; ++i) {
		char s[1001];
		scanf("%s", s);
		for (j = 0; j < w; ++j) {
			g[j][i] = s[j] - '0';
			c[j][i] = 0;
		}
	}

	long int nc = 2; // num colours
	for (i = 0; i < w; ++i) {
		for (j = 0; j < h; ++j) {
			if (c[i][j] <= 1) {
				++nc;
				colour(i, j, nc, g[i][j]);
			}
		}
	}

	int n;
	scanf("%d", &n);
	for (i = 0; i < n; ++i) {
		int k, l, m;
		scanf("%d %d %d %d", &j, &k, &l, &m);
		--j;
		--k;
		--l;
		--m;
		if (c[k][j] != c[m][l]) {
			printf("neither\n");
			continue;
		}
		if (g[k][j] == 1) {
			printf("decimal\n");
			continue;
		}
		printf("binary\n");
	}
}
