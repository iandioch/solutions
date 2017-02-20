#include <stdio.h>

int main() {
	int a, b, c, d;
	while (1) {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		if (a == 0 && b == 0 && c == 0 && d == 0) break;
		a *= 9;
		b *= 9;
		c *= 9;
		d *= 9;
		long int ans = 720; // 2 full turns
		ans += (a-b+360)%360;
		ans += 360;
		ans += (c-b+360)%360;
		ans += (c-d+360)%360;
		printf("%ld\n", ans);
	}
}
