#include <stdio.h>

int main() {
	char dom = 'a';
	int domval[] = { 11, 4, 3, 20, 10, 14, 0, 0 };
	int notval[] = { 11, 4, 3, 2, 10, 0, 0, 0 };
	int n;
	scanf("%d %c\n", &n, &dom);
	int i;
	long int sum = 0;
	for (i = 0; i < n*4; ++i) {
		char k, suit;
		scanf("%c%c\n", &k, &suit);
		int index = 0;
		switch(k) {
			case 'A':
				index = 0;
				break;
			case 'K':
				index = 1;
				break;
			case 'Q':
				index = 2;
				break;
			case 'J':
				index = 3;
				break;
			case 'T':
				index = 4;
				break;
			case '9':
				index = 5;
				break;
			case '8':
				index = 6;
				break;
			case '7':
				index = 7;
				break;
			default:
				index = -1;
		}
		if (suit == dom) {
			sum += domval[index];
		} else {
			sum += notval[index];
		}
	}
	printf("%ld\n", sum);
	return 0;
}
