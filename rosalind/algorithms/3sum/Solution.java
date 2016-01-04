import java.io.*;
import java.util.*;

class Solution{
	public static String get2Sum(int[] a){
		Map<Integer, Integer> locs = new HashMap<>();
		for(int i = 0; i < a.length; i ++){
			locs.put(a[i], i);
		}
		for(int i = 0; i < a.length-2; i ++){
			for(int j = i+1; j < a.length-1; j++){
				int x = - a[i] - a[j];
				if (locs.containsKey(x) && locs.get(x) > j) {
					return (i+1) + " " + (j+1) + " " + (locs.get(x)+1);
				}
				/*for(int k = j+1; k < a.length; k ++){
					if(a[i] + a[j] + a[k] == 0){
						return (i+1) + " " + (j+1) + " " + (k+1);
					}
				}*/
			}
		}
		return "-1";
	}
	public static void main(String[] args){
		try{
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			String[] parts = in.readLine().split("\\s+");
			int numTests = Integer.parseInt(parts[0]);
			int arrLength = Integer.parseInt(parts[1]);
			for(int i = 0; i < numTests; i ++){
				parts = in.readLine().split("\\s+");
				int[] a = new int[arrLength];
				for(int j = 0; j < arrLength; j ++){
					a[j] = Integer.parseInt(parts[j]);
				}
				System.out.println(get2Sum(a));
			}
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}