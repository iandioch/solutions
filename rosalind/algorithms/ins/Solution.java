import java.io.*;
import java.util.*;

class Solution{

	private static <T> void swap(T[] a, int i, int j){
		T x = a[i];
		a[i] = a[j];
		a[j] = x;
	}

	private static void swap(int[] a, int i, int j){
		int x = a[i];
		a[i] = a[j];
		a[j] = x;
	}
	private static int insertionSort(int[] a){
		int numSwaps = 0;
		for(int i = 1; i < a.length; i ++){
			int k = i;
			while (k > 0 && a[k] < a[k-1]) {
				swap(a, k-1, k);
				k --;
				numSwaps ++;
			}
		}
		return numSwaps;
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

			System.out.println(insertionSort(a));
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}