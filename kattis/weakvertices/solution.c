#include <stdio.h>

int main() {
	while (1) {
		int n;
		scanf("%d", &n);
		if (n < 0) return 0;
		int edge[n][n];
		int i;
		int j;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < n; ++j) {
				scanf("%d", &edge[i][j]);
			}
		}

		int found[n];
		for (i = 0; i < n; ++i) {
			found[i] = 0;
		}
		for (i = 0; i < n; ++i) {
			if (found[i] > 0) continue;
			for (j = 0; j < n; ++j) {
				if (edge[i][j] == 0) continue;
				/* edge between i and j,
				looking for a k such that there is
				an edge between i and k,
				and an edge between j and k. */	
				int k;
				for (k = 0; k < n; ++k) {
					if (k==i || k == j) continue;
					if (edge[j][k] > 0 && edge[i][k] > 0) {
						found[i] = 1;
						found[j] = 1;
						found[k] = 1;
						break;
					}
				}
			}
		}
		for (i = 0; i < n; ++i) {
			if (found[i] == 0) printf("%d ", i);
		}
		printf("\n");
	}
}
