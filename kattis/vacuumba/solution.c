#include <stdio.h>
#include <math.h>

#define PI 3.1415926525

int main() {
	int num_tests;
	scanf("%d", &num_tests);
	int test;
	for(test = 0; test < num_tests; ++test) {
		int num_segments;
		scanf("%d", &num_segments);
		int segment;
		long double x, y, rot;
		x = 0;
		y = 0;
		rot = 0;
		for(segment = 0; segment < num_segments; ++segment) {
			long double rotation, dist;
			scanf("%llf %llf", &rotation, &dist);
			rot += rotation;
			x += dist*sin(-rot*PI/180.0);
			y += dist*cos(-rot*PI/180.0);
		}
		printf("%llf %llf\n", x, y);
	}
	return 0;
}
