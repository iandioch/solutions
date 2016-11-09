import java.io.*;
import java.util.*;

class Solution {

	private static int[] copyArray(int[] in) {
		int[] out = new int[in.length];
		System.arraycopy(in, 0, out, 0, in.length);
		return out;
	}

	private static int solve(int[] a) {
		int i = 0;
		while (i < a.length) {
			if (a[i] == 0) break;
			i ++;
		}
		if (i == a.length) return a[0]*100 + a[1]*10 + a[2];

		int answer = -1;
		HashSet<Integer> taken = new HashSet<>();
		for (int p = 0; p < 81; p ++) {
			if ((p/9 == i/9) || // same row
			    ((p-i) % 9 == 0) || // same col
			    ((p/27 == i/27) && ((p%9)/3 == (i%9)/3))) { // same square
				taken.add(a[p]);
			}
		}

		for (int j = 1; j < 10; j ++) {
			if (taken.contains(j)) continue;
			int[] b = new int[81];
			System.arraycopy(a, 0, b, 0, 81);
			b[i] = j;
			int maybeAns = solve(b);
			if (maybeAns > 0) {
				return maybeAns;
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
				for (int i = 0; i < 9; i ++) {
					String s = in.readLine();
					for (int j = 0; j < 9; j ++) {
						a[i*9 + j] = s.charAt(j) - '0';
					}
				}
				int m = solve(a);
				total += m;
			}
			System.out.println(total);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
