#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max(a, b) a > b ? a : b

int t[1000000];

int comp (const void * a, const void * b) {
	int i = *((int*)a);
	int j = *((int*)b);
	return j-i;
}

int main () {
	memset(t, 0, sizeof(t));
	int n;
	scanf("%d", &n);
	int i;
	for (i = 0; i < n; ++i) {
		scanf("%d", &t[i]);
	}
	qsort(t,
	      sizeof(t)/sizeof(*t),
	      sizeof(*t), comp);
	int last_day = 0;
	for (i = 0; i < n; ++i) {
		last_day = max(last_day,
			       t[i]+i+1);
	}
	printf("%d\n", last_day+1);
}
