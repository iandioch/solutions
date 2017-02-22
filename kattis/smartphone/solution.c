#include <stdio.h>
#include <string.h>


char desired[30], s[4][30];

int try_s(int n) {
	int i = 0;
	while (i < strlen(desired) && i < strlen(s[n])) {
		if (desired[i] != s[n][i]) break;
		++i;
	}
	return strlen(&s[n][i]) + strlen(&desired[i]);
}

int run_case() {
	scanf("%s", desired);
	scanf("%s", s[0]);
	scanf("%s", s[1]);
	scanf("%s", s[2]);
	scanf("%s", s[3]);
	int best = try_s(0);

	int i;
	for (i = 1; i < 4; ++i) {
		int g = try_s(i) + 1;
		if (g < best) best = g;
	}
	return best;
}

int main() {
	int t;
	scanf("%d", &t);
	int it;
	for (it = 0; it < t; ++it) {
		printf("%d\n", run_case());
	}
}
