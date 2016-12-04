import java.util.*;

class Solution {

	static byte[] opt;
	static long basicc, optc;

	private static char[] digitalRoot(char[] c) {
		if (c.length == 1) return c;
		int ans = 0;
		for (int i = 0; i < c.length; i ++) {
			ans += c[i] - '0';
		}
		return (ans+"").toCharArray();
	}

	private static boolean[] sieve(int n) {
		boolean[] composite = new boolean[n];
		for (int i = 2; i < n; i ++) {
			if (!composite[i]) {
				for (int j = i+i; j < n; j += i) {
					composite[j] = true;
				}
			}
		}
		return composite;
	}

	public static void main(String[] args) {
		opt = new byte[32];
		basicc = 0;
		optc = 0; // count of changes

		/*
		*    0
		*  5   1
		*    6
		*  4   2
		*    3
		*/
		// pos    76543210
		byte[] on = {
			0b00111111, //0
			0b00000110, //1
			0b01011011, //2
			0b01001111, //3
			0b01100110, //4
			0b01101101, //5
			0b01111101, //6
			0b00100111, //7
			0b01111111, //8
			0b01101111, //9
		 };

		final int START = 10000000;
		boolean[] composite = sieve(2*START);
		for (int i = START; i < composite.length; i ++) {
			if (composite[i]) continue;

			char[] digits = (i+"").toCharArray();
			while (true) {
				for (int j = 0; j < digits.length; j ++) {
					final int k = digits[digits.length-j-1] - '0';
					basicc += Integer.bitCount(on[k])*2;
					optc += Integer.bitCount(opt[j] ^ on[k]);
					opt[j] = on[k];
				}
				// turn off every num that isn't used
				for (int j = digits.length; j < opt.length; j ++) {
					optc += Integer.bitCount(opt[j]);
					opt[j] = 0;
				}
				if (digits.length == 1) break;
				digits = digitalRoot(digits);
			}
			// turn off all segments
			for (int j = 0; j < opt.length; j ++) {
				optc += Integer.bitCount(opt[j]);
				opt[j] = 0;
			}
		}
		System.out.println(basicc-optc);
	}
}
