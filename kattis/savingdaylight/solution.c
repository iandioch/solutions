#include <stdio.h>

int main() {
	while (1) {
		char month[10];
		int day, year, rise_hour, rise_min, set_hour, set_min;
		scanf("%s", month);
		if (feof(stdin)) {
			break;
		}
		scanf("%d %d %d:%d %d:%d\n", &day, &year, &rise_hour, &rise_min, &set_hour, &set_min);
		int mindiff = 0;
		if (set_min < rise_min) {
			mindiff += 60 - rise_min + set_min;
			mindiff += 60*(set_hour - rise_hour - 1);
		} else {
			mindiff += set_min - rise_min; 
			mindiff += 60*(set_hour - rise_hour);
		}
		printf("%s %d %d %d hours %d minutes\n", month, day, year, mindiff/60, mindiff%60);
	}
	return 0;
}
