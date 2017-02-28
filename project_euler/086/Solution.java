import java.util.*;

class Solution {
	static Set<Long> squares;

	public static void main(String[] args) {
		squares = new HashSet<>();
		for (long i = 1; i < (long) Math.pow(2, 20); i++) {
			squares.add(i*i);
		}
		long ans = 0;
		long m = 0;
		while (ans < 1000000) {
			m ++;
			long z2 = m*m;
			
			for (long x = 1; x <= m; x++) {
				for (long y = x; y <= m; y++) {
					long d = (x+y)*(x+y);
					if (squares.contains(d + z2)) {
						ans ++;
					}
				}
			}
		}
		System.out.println(m);
	}
}
