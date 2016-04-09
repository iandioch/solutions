import java.util.*;

class Solution{

    public static boolean isPalindrome(int l){
        int rev = 0;
        int k = l;
        while(k > 0){
            rev = (10*rev) + (k%10);
            k /= 10;
        }
        return rev == l;
    }

    public static void main(String[] args){
        int max = 100000000;

        Set<Integer> s = new HashSet<>();
        long sum = 0;

        for(int i = 1; i*i < max; i ++){
            int n = i*i;
            for(int j = i + 1; j*j < max; j ++){
                n += j*j;
                if(n > max){
                    break;
                }

                if(isPalindrome(n) && !s.contains(n)){
                    s.add(n);
                    sum += n;
                }
            }
        }
        System.out.println(s);
        System.out.println(sum);
    }
}
