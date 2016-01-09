package main

import (
	"fmt"
	//"math"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a % b
	}
	return a
}

func main(){
	num := make([]int, 1500001)

    for m := 1; m*m*2 <= len(num); m ++ {
    	for n := 1; n < m; n ++ {
    		if gcd(m,n) != 1 || ((m-n)%2) != 1 {
    			continue
    		}
    		a := m*m - n*n
    		b := 2*m*n
    		c := m*m + n*n

    		for k := 1; ; k ++ {
	    		if k*(a+b+c) < len(num){
	    			num[k*(a+b+c)] += 1
	    		}else{
	    			break
	    		}

	    	}
    	}
    }


	ans := 0

	for _, n := range num {
		if n == 1 {
			ans ++
		}
	}

	fmt.Println(ans)
}