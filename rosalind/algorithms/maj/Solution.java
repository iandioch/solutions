import java.io.*;
import java.util.*;

class Solution{
	public static int majorityElement(int[] a){
		Map<Integer, Integer> count = new HashMap<>();
		for(int i = 0; i < a.length; i ++){
			Integer e = a[i];
			if (count.containsKey(e)){
				int newCount = count.get(e)+1;
				if(newCount > a.length/2){
					return a[i];
				}
				count.put(e, newCount);
			}else{
				count.put(e, 1);
			}
		}
		return -1;
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
				System.out.print(majorityElement(a) + " ");
			}
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}