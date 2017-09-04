#include <stdio.h>

int main () {
	int a, b, c, d, e;
	scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
	int des = c*(b-a);
	int req = des/e;   
	if (req * e <= des) ++req;
	printf("%d\n", d + req);
	return 0;
}
