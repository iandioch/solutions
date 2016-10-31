import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

class Solution{
	static Map<String, Integer> numerals;

	private static int romanToInt(String s) {
		int ans = 0;
		char[] c = s.toCharArray();
		int i = 0;
		while (i < s.length() - 1) {
			String t = c[i] + "" + c[i+1];
			if(numerals.containsKey(t)) {
				ans += numerals.get(t);
				i += 2;
			} else {
				ans += numerals.get(c[i] + "");
				i ++;
			}
		}
		if (i < s.length()) {
			ans += numerals.get(c[i] + "");
		}
		return ans;
	}

	private static List<String> getSortedNumerals() {
		List<String> sorted = new ArrayList<>(numerals.keySet());
		sorted.sort((a, b) -> numerals.get(a).compareTo(numerals.get(b)));
		return sorted;
	}
	
	private static String intToRoman(int a){
		List<String> sorted = getSortedNumerals();
		StringBuilder ans = new StringBuilder();
		int curr = sorted.size()-1;
		int v = a+0;
		while(v > 0) {
			if (numerals.get(sorted.get(curr)) <= v) {
				ans.append(sorted.get(curr));
				v -= numerals.get(sorted.get(curr));
			} else {
				curr --;
			}
		}
		return ans.toString();
	}

	public static void main(String[] args) throws IOException {
		numerals = new HashMap<>();
		numerals.put("I", 1);
		numerals.put("IV", 4);
		numerals.put("V", 5);
		numerals.put("IX", 9);
		numerals.put("X", 10);
		numerals.put("XL", 40);
		numerals.put("L", 50);
		numerals.put("XC", 90);
		numerals.put("C", 100);
		numerals.put("CD", 400);
		numerals.put("D", 500);
		numerals.put("CM", 900);
		numerals.put("M", 1000);

		int diff = 0;

		BufferedReader in = new BufferedReader(new FileReader(args[0]));
		String line = in.readLine();
		while (line != null) {
			String s = intToRoman(romanToInt(line));
			diff += line.length() - s.length();
			line = in.readLine();
		}
		System.out.println(diff);
	}
}
