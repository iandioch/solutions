#include <stdio.h>
#include <math.h>

double get_prob(int total_rounds, int curr_round, int blues, int reds) {
	if (curr_round == total_rounds) {
		return blues > reds ? 1 : 0;
	}

	// if we draw a blue here 
	double a = get_prob(total_rounds,
			    curr_round + 1,
			    blues + 1,
			    reds) / (curr_round + 2);
	// (curr_round+1)/(curr_round+2) odds of drawing a red
	a += (curr_round + 1) * get_prob(total_rounds,
		      			 curr_round + 1,
		      			 blues,
		      			 reds + 1) / (curr_round + 2);
}

int main() {
	printf("%d\n", (int)floor(1/get_prob(15, 0, 0, 0)));
	return 0;
}
