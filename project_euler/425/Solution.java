import java.util.*;

class Solution {
	static int LIM = 10000000;
	static List<Integer> primes;
	static HashSet<Integer> primeSet;
	static HashSet<String> primeStringSet;
	static Map<String, Vertex> stringToVertex;

	static TreeSet<Integer> toSearch;
	static Set<Integer> been;
	static Set<Integer> beenOrGoing;

	static Set<Integer> hasPathTo2 = new HashSet<>(); // highest num encountered in path from K to 2

	static class Vertex {
		int q;
		Set<Vertex> e;

		public Vertex(int q) {
			this.q=q;
			this.e = new HashSet<>();
		}

		public void addEdge(Vertex other) {
			e.add(other);
		}
	}

	static List<String> getPoss(int q, int max) {
		List<String> poss = new ArrayList<>();
		String s = q+"";
		for (int i = 0; i < 10; i++) {
			String t = i + s;
			if (primeStringSet.contains(t)) {
				poss.add(t);
			}
		}
		if (primeStringSet.contains(s.substring(1))) {
			poss.add(s.substring(1));
		}
		for (int p : primes) {
			if (p >= max) break;
			if (p == q) continue;
			String t = p+"";
			int sl = s.length();
			int tl = t.length();
			if (sl != tl) {
				continue;
			}
			int diff = 0;
			for (int i = 0; i < sl; ++i) {
				if (s.charAt(i) != t.charAt(i)) diff++;
			}
			if (diff == 1) {
				poss.add(t);
			}
		}
		return poss;
	}

	static void sieve() {
		boolean[] is_composite = new boolean[LIM];
		primes = new ArrayList<>();
		int i, j;
		for (i = 2; i < LIM; i++) {
			if (!is_composite[i]) {
				primes.add(i);
				for (j = i+i; j < LIM; j+=i) {
					is_composite[j] = true;
				}
			}
		}
	}

	public static void main(String[] args) {
		sieve();
		primeSet = new HashSet<>(primes);
		primeStringSet = new HashSet<>();
		for (int p : primes) {
			primeStringSet.add(p+"");
		}

		System.out.println("Have primes");

		long total = 0;
		for (int ip = 0; ip < primes.size(); ip++) {
			int i = primes.get(ip);
			toSearch = new TreeSet<>();
			been = new HashSet<>();
			beenOrGoing = new HashSet<>();
			toSearch.add(i);
			boolean found2 = false;
			int j = 0;
			while (j < toSearch.size()) {
				int v = toSearch.pollFirst();
				j = 0;
				if (been.contains(v)) {
					continue;
				}
				been.add(v);
				if (v == 2) {
					found2 = true;
					for (int q : been) {
						hasPathTo2.add(q);
					}

					break;
				}
				for (String w : getPoss(v, i)) {
					int x = Integer.parseInt(w);
					if (hasPathTo2.contains(x)) {
						// quit
						found2 = true;
						j = toSearch.size() + 10;
						for (int q : been) {
							hasPathTo2.add(q);
						}
						break;
					} 
					if (x < i && !beenOrGoing.contains(x)){
						toSearch.add(x);
						beenOrGoing.add(x);
					}
				}
			}
			if (!found2){
				total += i;
				System.out.println(i);
			}
		}
		System.out.println(total);
	}
}
