import java.io.*;
import java.util.*;

class Solution{
	public static void main(String[] args){
		if (args.length != 1) {
			System.out.println("Please provide an input n, to get the n'th fibonacci number.");
		}
		try{
			int n = Integer.parseInt(args[0]);

			long a = 0;
			long b = 1;
			long c = 1;

			for(int i = 1; i < n; i ++){
				c = a+b;
				a = b;
				b = c;
			}

			System.out.println(c);
		}catch(NumberFormatException e){
			e.printStackTrace();
		}
	}
}