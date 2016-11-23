#include <stdio.h>
#include <string.h>

int main() {
	int n, s, r;
	scanf("%d %d %d", &n, &s, &r);
	int damaged[n+2];
	memset(damaged, 0, sizeof(damaged));
	int reserve[n+2];
	memset(reserve, 0, sizeof(reserve));
	int i;

	for (i = 0; i < s; i ++) {
		int t;
		scanf("%d", &t);
		damaged[t] = 1;
	}
	for (i = 0; i < r; i ++) {
		int t;
		scanf("%d", &t);
		reserve[t] = 1;
	}
	int ans = 0;
	for (i = 1; i <= n; i ++) {
		if (damaged[i] > 0) {
			if (reserve[i]) {
				reserve[i] = 0;
			} else if (reserve[i-1]) {
				/* cool beans */
			} else if (reserve[i+1]) {
				reserve[i+1] = 0;
			} else {
				ans ++;
			}
		}
	}
	printf("%d\n", ans);
	
}
