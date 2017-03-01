#include <stdio.h>

int main() {
	int d[] = {1, 1, 2, 2, 2, 8};
	int h[6];
	scanf("%d %d %d %d %d %d", &h[0], &h[1], &h[2], &h[3], &h[4], &h[5]);
	int i;
	for (i = 0; i < 6; ++i) {
		printf("%d ", d[i] - h[i]);
	}
	return 0;
}
