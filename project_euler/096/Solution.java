// Brute force, same logic as Python solution. Runs in < 4 seconds

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.BitSet;

class Solution {
	private static int solve(int[] a) {
		int i = 0;
		while (i < a.length && a[i] != 0) {
			i ++;
		}
		if (i == a.length) return a[0]*100 + a[1]*10 + a[2];

		BitSet taken = new BitSet(10);
		for (int p = 0; p < 81; p ++) {
			if ((p/9 == i/9) || // same row
			    ((p-i) % 9 == 0) || // same col
			    ((p/27 == i/27) && ((p%9)/3 == (i%9)/3))) { // same square
				taken.set(a[p]);
			}
		}

		for (int j = 1; j < 10; j ++) {
			if (taken.get(j)) continue;
			int[] b = new int[81];
			System.arraycopy(a, 0, b, 0, 81);
			b[i] = j;
			int answer = solve(b);
			if (answer > 0) {
				return answer;
			}
		}
		return -1;
	}

	public static void main(String[] args) {
		try {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			int total = 0;
			for (int n = 0; n < 50; n ++) {
				in.readLine();
				int[] a = new int[81];
				int curr = 0;
				for (int i = 0; i < 9; i ++) {
					String s = in.readLine();
					for (int j = 0; j < 9; j ++) {
						a[curr] = s.charAt(j) - '0';
						curr ++;
					}
				}
				total += solve(a);
			}
			System.out.println(total);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
