#include <stdio.h>

int main() {
	long long int dp[31];
	int i;
	for (i = 0; i < 31; ++i) {
		dp[i] = 0;
	}
	dp[0] = 1;
	dp[2] = 3;
	for (i = 4; i < 31; ++i) {
		dp[i] = 4*dp[i-2] - dp[i-4];
	}
	while (1) {
		int n;
		scanf("%d", &n);
		if (n < 0) break;
		printf("%lld\n", dp[n]);
	}
	return 0;
}
