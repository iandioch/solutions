#include <stdio.h>
#include <string.h>

int main() {
	char s[1000];
	scanf("%s", &s);
	int up = 0;
	int down = 0;
	int pref = 0;
	int len = strlen(s);
	int prev = s[0];
	for(int i = 1; i < len; i ++){
		if (prev != s[i]){ 
			up ++;
			prev = s[i];
		}
		if (prev != 'U') {
			up ++;
			prev = 'U';
		}
	}
	prev = s[0];
	for(int i = 1; i < len; i ++){
		if (prev != s[i]){ 
			down ++;
			prev = s[i];
		}
		if (prev != 'D') {
			down ++;
			prev = 'D';
		}
	}
	prev = s[0];
	for(int i = 1; i < len; i ++){
		if (prev != s[i]){ 
			pref ++;
			prev = s[i];
		}
	}
	printf("%d\n", up);
	printf("%d\n", down);
	printf("%d\n", pref);
}
