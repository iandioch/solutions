#include <stdio.h>

int main() {
	int h, w, n;
	scanf("%d %d %d", &h, &w, &n);
	int b[10000];
	int i;
	for(i = 0; i < n; i ++){
		int c;
		scanf("%d", &c);
		b[i] = c;
	}
	i = 0;
	int cw = 0;
	int ch = 0;
	while (1) {
		int c = b[i];
		if (cw + c < w) {
			cw += c;
		} else if (cw + c > w) {
			printf("NO\n");
			break;
		} else {
			ch ++;
			cw = 0;
			if (ch == h) {
				printf("YES\n");
				break;
			}
		}
		i ++;	
		if (i == n) {
			printf("NO\n");
			break;
		}
	}
	return 0;
}
