#include <stdio.h>
#include <string.h>

int main() {
	char able[1001], req[1001];
	scanf("%s", able);
	scanf("%s", req);
	if (strlen(able) >= strlen(req)) {
		printf("go\n");
	} else {
		printf("no\n");
	}
}
