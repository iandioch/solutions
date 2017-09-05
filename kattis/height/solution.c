#include <stdio.h>

int main () {
	int num_tests;
	scanf("%d\n", &num_tests);
	int test;
	int heights[20];
	for (test = 1; test <= num_tests; ++test) {
		int k;
		scanf("%d", &k);
		int curr_student;
		long long ans = 0;
		int h;
		scanf("%d", &heights[0]);
		for (curr_student = 1; curr_student < 20; ++curr_student) {
			scanf("%d", &h);
			int j = 0;
			while (j < curr_student && heights[j] <= h) {
				++j;
			}
			int k;
			for (k = curr_student; k > j; --k) {
				heights[k] = heights[k-1];	
				++ans;
			}
			heights[j] = h;
		}
		printf("%d %lld\n", k, ans);
	}
	return 0;
}
