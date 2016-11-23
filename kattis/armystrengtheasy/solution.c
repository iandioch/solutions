#include <stdio.h>
#include <stdlib.h>

int comp(const void * elem1, const void * elem2) {
	int f = *((int*) elem1);
	int s = *((int*) elem2);
	return f-s;
}

int main() {
	int tests;
	scanf("%d", &tests);
	int test;
	for (test = 0; test < tests; test ++) {
		int g, m;
		scanf("%d %d", &g, &m);
		int ga[g], ma[m];
		int i;
		for (i = 0; i < g; i ++) {
			scanf("%d", &ga[i]);
		}
		for (i = 0; i < m; i ++) {
			scanf("%d", &ma[i]);
		}

		qsort(ga, sizeof(ga)/sizeof(*ga), sizeof(*ga), comp);
		qsort(ma, sizeof(ma)/sizeof(*ma), sizeof(*ma), comp);
		i = 0;
		int j = 0;
		while (1) {
			if (ma[j] <= ga[i]) {
				j ++;
			} else {
				i ++;
			}
			if (j == m) {
				printf("Godzilla\n");
				break;
			}
			if (i == g) {
				printf("MechaGodzilla\n");
				break;
			}
		}
	}
}
