#include <stdio.h>

int main() {
	long int n;
	while (scanf("%ld", &n) != EOF) {
		if (n == 0) printf("0\n");
		else if (n == 1) printf("1\n");
		else printf("%ld\n", n+n-2);
	}
}
