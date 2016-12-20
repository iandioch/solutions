#include <stdio.h>
#include <string.h>

int main () {
	char s[100000];
	scanf("%s", s);
	int i;
	int tot = 0;
	int whitespace = 0;
	int lower = 0;
	int upper = 0;
	int symbol = 0;
	for(i = 0; i < 1000000; ++i) {
		if (s[i] == '\0') {
			break;
		} else if (s[i] == '_') {
			++whitespace;
		} else if (s[i] >= 'a' && s[i] <= 'z') {
			++lower;
		} else if (s[i] >= 'A' && s[i] <= 'Z') {
			++upper;
		} else {
			++symbol;
		}
		++ tot;
	}
	double n = tot;
	printf("%lf\n%lf\n%lf\n%lf\n", whitespace/n, lower/n, upper/n, symbol/n); 
	return 0;
}
