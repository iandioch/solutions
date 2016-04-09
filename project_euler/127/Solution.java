import java.util.*;

class Solution{
    private static long gcd(long a, long b){
        while(b != 0){
            long t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    public static void main(String[] args){
        long[] rad = new long[120001];
        for(int i = 0; i < rad.length; i ++) rad[i] = 1;
        for(int i = 2; i < rad.length; i ++){
            if(rad[i] != 1) continue;
            rad[i] = i;
            for(int j = i+i; j < rad.length; j += i){
                rad[j] *= i;
            }
        }

        int max = 120000;
        long c_sum = 0;
        for(int a = 1; a < max; a ++){
            for(int b = a+1; a+b < max; b++){
                if(rad[a]*rad[b]*rad[a+b] >= a+b) continue;
                if(gcd(a, b) != 1) continue;
                c_sum += a+b;
            }
        }
        System.out.println(c_sum);
    }
}
