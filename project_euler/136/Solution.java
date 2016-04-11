import java.util.*;

class Solution{
    public static void main(String[] args){
        int[] n = new int[50000000];
        for(int z = 1; z < n.length; z ++){
            for(int d = z/3 + 1; d < n.length; d ++){
                int m = 2*d*z + 3*d*d - z*z;
                if(m < 0){
                    //System.out.println(z + " " + d);
                    break;
                }
                if (m >= n.length){
                    continue;
                }
                n[m] += 1;
            }
        }
        int ans = 0;
        for(int i : n){
            if(i == 1){
                ans ++;
            }
        }
        
        System.out.println(ans);
    }
}
