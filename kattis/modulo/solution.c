#include <stdio.h>
#include <string.h>

int main () {
	int found [1000];
	memset(found, 0, sizeof(found));
	int i;
	for (i = 0; i < 10; ++i) {
		int n;
		scanf("%d", &n);
		found[n%42] = 1;
	}
	int tot = 0;
	for (i = 0; i < 1000; ++i) {
		if (found[i] > 0) ++tot;
	}
	printf("%d\n", tot);
	return 0;
}
