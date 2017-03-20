#include <stdio.h>
#define abs(a) ((a) < 0 ? -(a) : (a))

int main() {
	long long int a, b;
	scanf("%lld %lld", &a, &b);

	char *pieces = "pieces";
	if (abs(a-b) == 1) {
		pieces = "piece";
	}
	if (a > b) {
		printf("Dr. Chaz needs %lld more %s of chicken!\n", a-b, pieces);
	} else {
		printf("Dr. Chaz will have %lld %s of chicken left over!\n", b-a, pieces);
	}
	return 0;
}
