#include <stdio.h>
#include <string.h>

int main() {
	long int n, k;
	scanf("%ld %ld", &n, &k);
	int arr[100001];
	memset(arr, 0, sizeof(arr));
	long int i, j;
	long int ans = 1;
	for (i = 2; i <= n; ++i) {
		if (!arr[i]) {
			// prime!
			for (j = i; ; j += i) {
				if (j > n) break;
				if (!arr[j]) {
					if (ans == k) {
						printf("%ld\n", j);
						return 0;
					}
					arr[j] = 1;
					++ans;
				}
			}
		}
	}
	return 0;
}
