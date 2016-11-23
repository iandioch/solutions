#include <stdio.h>
#include <stdlib.h>

int comp(const void * elem1, const void * elem2) {
	unsigned long int f = *((unsigned long int*) elem1);
	unsigned long int s = *((unsigned long int*) elem2);
	if (f > s) return 1;
	if (f < s) return -1;
	return 0;
}

int main() {
	int tests;
	scanf("%d", &tests);
	int test;
	for (test = 0; test < tests; test ++) {
		unsigned long int g, m;
		scanf("%lu %lu", &g, &m);
		unsigned long int ga[g], ma[m];
		unsigned long int i;
		for (i = 0; i < g; i ++) {
			scanf("%lu", &ga[i]);
		}
		for (i = 0; i < m; i ++) {
			scanf("%lu", &ma[i]);
		}

		qsort(ga, sizeof(ga)/sizeof(*ga), sizeof(*ga), comp);
		qsort(ma, sizeof(ma)/sizeof(*ma), sizeof(*ma), comp);
		i = 0;
		unsigned long int j = 0;
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
