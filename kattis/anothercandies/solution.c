#include <stdio.h>

int main() {
	int t;
	scanf("%d", &t);
	int ct;
	for (ct = 0; ct < t; ct ++) {
		int n;
		scanf("%d", &n);
		unsigned long long c = 0;
		int i;
		for (i = 0; i < n; i ++) {
			unsigned long long d;
			scanf("%llu", &d);
			c += (d%n);
			c %= n;
		}
		if (c == 0) printf("YES\n");
		else printf ("NO\n");
	}
}
