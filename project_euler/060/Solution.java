import java.util.*;

class Solution {

	private static List<Integer> sieve (int n) {
		boolean[] isComposite = new boolean[n];
		List<Integer> primes = new ArrayList<>();
		for (int i = 2; i < n; i++) {
			if (!isComposite[i]) {
				primes.add(i);
				for (int j = i+i; j < n; j += i) {
					isComposite[j] = true;
				}
			}
		}
		return primes;
	}
	
	public static void main (String[] args) {
		final int target = 5;
		List<Integer> primes = sieve(Integer.MAX_VALUE/25);
		Set<Integer> primeSet = new HashSet<>(primes);
		Set<Set<Integer>> set = new HashSet<>();

		int minSum = Integer.MAX_VALUE;
		for (int i = 0; i < 2000; i ++) {
			int a = primes.get(i);
			Set<Set<Integer>> newSet = new HashSet<>();
			for (Set<Integer> s : set) {
				boolean valid = true;
				for (int b : s) {
					int c = Integer.parseInt(a + "" + b);
					if (!primeSet.contains(c)) {
						valid = false;
						break;
					}
					int d = Integer.parseInt(b + "" + a);
					if (!primeSet.contains(d)) {
						valid = false;
						break;
					}
				}
				if (valid) {
					Set<Integer> t = new HashSet<>(s);
					t.add(a);
					if (t.size() == target) {
						System.out.println(t);
						int sum = 0;
						for (int x : t) {
							sum += x;
						}
						System.out.println(sum);
						return;
					}
					newSet.add(t);
				}
			}
			for (Set<Integer> s : newSet) {
				set.add(s);
			}
			Set<Integer> n = new HashSet<>();
			n.add(a);
			set.add(n);
		}
	}

}
