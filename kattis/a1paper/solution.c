#include <stdio.h>
#include <math.h>

int main() {
	/* length and width of an a2 sheet (for all values below, length > width) */
	double length = pow(2, -3.0/4), width = pow(2, -5.0/4);
	int n;
	scanf("%d", &n);
	int i;
	double tot = 0.0;
	int needed = 1;
	for (i = 2; i < n + 1; ++i) {
		needed *= 2;
		int q;
		scanf("%d", &q);

		double perimeter = 2*(length+width);
		if (q >= needed) {
			tot += needed*perimeter;
			needed = 0;
		} else {
			tot += q*perimeter;
			needed -= q;
		}
		double newlength = width;
		width = length/2;
		length = newlength;
	}
	if (needed == 0) {
		/* the value tot contains the perimeters of every rect that makes up our A1 sheet.
		When you subtract the perimeter of the A1 sheet itself you get a value that
		only represents the edges that were glued. However, each edge is counted twice, once
		for each constituent sheet, so divide by 2 to get the final answer. */
		double ans = (tot - 2*(pow(2, -1.0/4) + pow(2, -3.0/4)))/2;
		printf("%.8f\n", ans);
	} else {
		printf("impossible\n");
	}
	return 0;
}
