#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int nums[6];
	int i;
	for(i = 0; i < 6; ++i) {
		nums[i] = 0;
	}
	int rolls[n];
	for(i = 0; i < n; ++i) {
		int t;
		scanf("%d", &t);
		rolls[i] = t;
		++nums[t-1];
	}
	int found = 0;
	for(i = 5; i >= 0; --i) {
		if (nums[i] == 1) {
			found = 1;
			int j;
			for (j = 0; j < n; ++j) {
				if (rolls[j] - 1 == i) {
					printf("%d\n", j+1);
					break;
				}
			}
			break;
		}
	}
	if (found == 0) {
		printf("none\n");
	}
}
