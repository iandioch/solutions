#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	int achance[202], bchance[202];
	memset(achance, 0, sizeof(achance));
	memset(bchance, 0, sizeof(bchance));
	int a, b, c, d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	int i, j;
	for (i = a; i <= b; ++i) {
		for (j = c; j <= d; ++j) {
			++achance[i+j];
		}
	}
	int e, f, g, h;
	scanf("%d %d %d %d", &e, &f, &g, &h);
	for (i = e; i <= f; ++i) {
		for (j = g; j <= h; ++j) {
			++bchance[i+j];
		}
	}
	long long numAWin = 0;
	long long numBWin = 0;
	for (i = 0; i < 201; ++i) {
		for (j = 0; j < 201; ++j) {
			if (i > j) numAWin += achance[i] * bchance[j];
			else if (i < j) numBWin += achance[i] * bchance[j];
		}
	}
	if (numAWin == numBWin) {
		printf("Tie\n");
	} else if (numAWin > numBWin) {
		printf("Gunnar\n");
	} else {
		printf("Emma\n");
	}
	return 0;
}
