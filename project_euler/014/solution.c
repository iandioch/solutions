#include <stdio.h>
#include <string.h>

#define LIM 1000000

long long len[LIM];

long long get_len(long long n) {
	long long ans = 0;
	while (n > 1) {
		if (n < LIM && len[n]) return ans + len[n];
		++ans;
		if (n % 2 == 0) n /= 2;
		else n = (3*n) + 1;
	}
	return ans;
}

int main() {
	memset(len, 0, sizeof(len));
	long long max = 0;
	int maxi = 0;
	int i;
	for (i = 2; i < LIM; ++i) {
		long long j = get_len(i);
		if (j > max) {
			max = j;
			maxi = i;
		}
	}
	printf("%d\n", maxi);
}
