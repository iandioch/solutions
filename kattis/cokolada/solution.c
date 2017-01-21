#include <stdio.h>

int main() {
	unsigned long int k; // 32 bits of goodness
	scanf("%lu", &k);
	int i;
	int first = -1;
	int last = -1;
	for (i = 0; i < 32; ++i) {
		unsigned long int d = 1 << (64-i-1);
		if (k & d) {
			if (first < 0) first = i;
			last = i;
		}
	}
	int numCuts = 1 + last-first;
	unsigned long int barSize = 1<<(64-first);
	if (numCuts == 1) {
		// there'll be a bar of this size anyway
		numCuts = 0;
		barSize = barSize >> 1;
	}
	printf("%lu %d\n", barSize, numCuts);
	return 0;
}
