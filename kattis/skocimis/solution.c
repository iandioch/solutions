#include <stdio.h>
#define min(a, b) (a < b ? a : b)
#define minarr(d) (min(d[0], min(d[1], d[2])))

int pos[3];

inline void swap(int i, int j) {
	int tmp = pos[i];
	pos[i] = pos[j];
	pos[j] = tmp;
}

void sortpos() {
	if (pos[0] > pos[1]) swap(0, 1);
	if (pos[1] > pos[2]) swap(1, 2);
	if (pos[0] > pos[1]) swap(0, 1);
}

int main() {
	scanf("%d %d %d", &pos[0], &pos[1], &pos[2]);
	sortpos();
	int adiff = pos[1] - pos[0];
	int bdiff = pos[2] - pos[1];
	int ans = 0;
	while (pos[2] - pos[0] > 2) {
		if (adiff > bdiff) {
			pos[2] = pos[0] + 1;
		} else {
			pos[0] = pos[1] + 1;
		}
		sortpos();
		adiff = pos[1] - pos[0];
		bdiff = pos[2] - pos[1];
		++ans;
	}
	printf("%d\n", ans);
	return 0;
}
