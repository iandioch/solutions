import java.util.*;

class Solution{

    public static Long[] sieve(int n){
        boolean[] isComp = new boolean[n];
        ArrayList<Long> primes = new ArrayList<>();
        for(int i = 2; i < n; i ++){
            if(!isComp[i]){
                primes.add(i+0L);
                for(int j = i+i; j < n; j += i){
                    isComp[j] = true;
                }
            }
        }
        return primes.toArray(new Long[primes.size()]);
    }
    public static void main(String[] args){
        final int max = 50000000;
        Long[] primes = sieve((int) Math.sqrt(max));
        primes = sieve(max);
        List<Long> cubes = new ArrayList<>();
        List<Long> quads = new ArrayList<>();
        for(long i : primes){
            if(i*i*i > max){
                break;
            }
            cubes.add(i*i*i);
            if(i*i*i*i <= max){
                quads.add(i*i*i*i);
            }
        }

        
        int num = 0;
        Set<Long> a = new HashSet<>();
        for(long i : primes){
            for(long k : quads){
                if((i*i) + k>max) break;
                for(long j : cubes){
                    if(((i*i) + j + k) < max){
                        a.add((i*i + j + k));
                    }else{
                        break;
                    }
                }
            }
        }
        //System.out.println(a);
        System.out.println(a.size());
    }
}
