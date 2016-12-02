#include <stdio.h>

int angry(int aggressive, int calm, int time) {
	time --;
	int t = time % (aggressive+calm);
	return t < aggressive;
}

char* count_dogs(int a, int b, int c, int d, int time) {
	int n = 0;
	if (angry(a, b, time)) n ++;
	if (angry(c, d, time)) n ++;
	switch (n) {
		case 0:
			return "none";
		case 1:
			return "one";
		case 2:
			return "both";
	}
	return "help me";
}

int main() {
	int a, b, c, d;
	scanf("%d %d %d %d", &a, &b, &c, &d);
	int p, m, g;
	scanf("%d %d %d", &p, &m, &g);
	printf("%s\n", count_dogs(a, b, c, d, p));
	printf("%s\n", count_dogs(a, b, c, d, m));
	printf("%s\n", count_dogs(a, b, c, d, g));
}
