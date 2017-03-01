import java.util.*;

class Solution {
	static final long BILLION = 1_000_000_000;

	public static void main(String[] args) {
		long ans = 0;

		/*
		 * A suitable triangle will have to be made up of two
		 * back-to-back pythagorean-triple-based triangles.
		 */
		long a = 3;
		long b = 4;
		long c = 5;
		long p;
		long na, nb, nc;
		while (true) {
			// almost-equilateral triangle has sides a,a,2c
			// perimiter is 2*(a+c)
			p = 2*(a+c);
			if (p >= BILLION) break;
			ans += p;

			/*
			 * Generate next pythagorean triple by Berggren's
			 * parent/child relationships:
			 * https://en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships
			 * This is T3 from the above, but with na and 
			 * nb swapped
			 */
			na = -2*a + b + 2*c;
			nb = -a + 2*b + 2*c;
			nc = -2*a + 2*b + 3*c;
			a = na;
			b = nb;
			c = nc;
		}
		System.out.println(ans);
	}
}
