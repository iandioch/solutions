#include <stdio.h>
#include <string.h>

int iter() {
	long int n, m;
	scanf("%ld %ld", &n, &m);
	if (feof(stdin)) return 0;
	long int move[11];
	long int i;
	for (i = 0; i < m; ++i) {
		scanf("%ld", &move[i]);
	}
	int stan[1000001];
	//memset(stan, 0, sizeof(stan));
	long int j;
	stan[0] = 0;
	for(i = 1; i <= n; ++i) {
		stan[i] = 0;
		for(j = 0; j < m; ++j) {
			if (i - move[j] < 0) continue;
			if (!stan[i-move[j]]) {
				stan[i] = 1;
				break;
			}
		}
	}
	if (stan[n] > 0) {
		printf("Stan wins\n");
	} else {
		printf("Ollie wins\n");
	}
	return 1;
}

int main() {
	while(!feof(stdin) && iter()){}
	return 0;
}
