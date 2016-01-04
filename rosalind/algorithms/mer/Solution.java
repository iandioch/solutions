import java.io.*;
import java.util.*;

class Solution{
	private static int[] merge(int[] a, int[] b, int x, int y){
		int[] result = new int[a.length + b.length];
		int index = 0;
		while(index < result.length){
			if(x == a.length){
				result[index] = b[y];
				y ++;
			}else if(y == b.length){
				result[index] = a[x];
				x ++;
			}else{
				if(a[x] < b[y]){
					result[index] = a[x];
					x ++;
				}else{
					result[index] = b[y];
					y++;
				}
			}
			index ++;
		}
		return result;
	}


	public static void main(String[] args){
		try{
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			int n = Integer.parseInt(in.readLine());
			String[] parts = in.readLine().split("\\s+");
			int[] a = new int[n];
			for(int i = 0; i < n; i ++){
				a[i] = Integer.parseInt(parts[i]);
			}

			int m = Integer.parseInt(in.readLine());
			parts = in.readLine().split("\\s+");
			int[] b = new int[m];
			for(int i = 0; i < m; i ++){
				b[i] = Integer.parseInt(parts[i]);
			}

			int[] result = merge(a, b, 0, 0);
			for(int i = 0; i < result.length; i ++){
				System.out.print(result[i] + " ");
			}
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}