import java.util.*;

class Solution{
	static Set<Integer> squares;
	final static int m = 100;
	static int[][] gcdMemo;
	static int[][] innerPointsMemo;

	static int gcdOrdered(int a, int b){
		if(b == 0){
			return a;
		}
		return gcdOrdered(b, a % b);
	}

	static int gcd(int a, int b){
		if(a>b){
			return gcdOrdered(a,b);
		}
		return gcdOrdered(b,a);
	}

	// get the number of points inside the triangle with the given width and height
	static int getInnerPoints(int w, int h){
		return ((h-1)*(w-1) - (gcdMemo[w][h] - 1))/2;
	}

	public static void main(String[] args){
		squares = new HashSet<Integer>();
		for(int i = 1; i < 10000; i ++){
			squares.add(i*i);
		}

		gcdMemo = new int[m+1][m+1];
		innerPointsMemo = new int[m+1][m+1];
		for(int i = 1; i < m + 1; i ++){
			for(int j = i; j < m + 1; j ++){
				int ans = gcd(j,i);
				gcdMemo[i][j] = ans;
				gcdMemo[j][i] = ans;

				int inner = getInnerPoints(i, j);
				innerPointsMemo[i][j] = inner;
				innerPointsMemo[j][i] = inner;
			}
		}

		int num = 0;

		int ab, abc, abcd = 0;

		for(int a = 1; a <= m; a ++){
			for(int b = 1; b <= m; b ++){
				ab = a + b + innerPointsMemo[a][b];
				for(int c = 1; c <= m; c ++){
					abc = ab + c + innerPointsMemo[b][c];
					for(int d = 1; d <= m; d ++){
						abcd = abc + d + innerPointsMemo[c][d] + innerPointsMemo[d][a] - 3; // subtract 3 because (0,0) has been counted 4 times
						if(squares.contains(abcd)){
							num ++;
						}
					}
				}
			}
		}
		System.out.println(num);
	}
}