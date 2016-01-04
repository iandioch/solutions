import java.io.*;
import java.util.*;

class Solution{

	private static int binSearch(int[] arr, int k, int start, int end){
		//int result = -1;
		int mid = start + (end-start)/2;
		if(start == end){
			if(arr[start] == k){
				return start;
			}else{
				return -2; // it will be incremented later
			}
		}
		if(arr[mid] == k){
			return mid;
		}else if(k < arr[mid]){
			return binSearch(arr, k, start, mid);
		}else{
			return binSearch(arr, k, mid+1, end);
		}
		//return result;
	}

	public static void main(String[] args){
		try{
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

			int n = Integer.parseInt(in.readLine());
			int m = Integer.parseInt(in.readLine());

			String[] parts = in.readLine().split("\\s+");
			int[] arr = new int[n];
			for(int i = 0; i < n; i ++){
				arr[i] = Integer.parseInt(parts[i]);
			}

			parts = in.readLine().split("\\s+");
			//System.out.println(parts);
			int[] k = new int[m];
			for(int i = 0; i < m; i ++){
				k[i] = Integer.parseInt(parts[i]);
			}
			int[] answers = new int[m];

			for(int i = 0; i < m; i ++){
				answers[i] = binSearch(arr, k[i], 0, n) + 1;
				System.out.print(answers[i] + " ");
			}
			System.out.println();
		}catch(IOException e){
			e.printStackTrace();
		}
	}
}