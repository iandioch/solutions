#include <stdio.h>
#include <math.h>
#define min(a, b) a < b ? a : b

int main() {
	int d;
	long long money = 100;
	int prev = 1<<31;
	scanf("%d", &d);
	int i;
	for(i = 0; i < d; ++i) {
		int now;
		scanf("%d", &now);
		if (now > prev) {
			long long numStocks = min(money/prev, 100000);
			money += numStocks*(now-prev);
		}
		prev = now;
	}
	printf("%lld\n", money);
}
