package main

import (
	"fmt"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a % b
	}
	return a
}

func diff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}
// modified #75

func main(){
	//num := make([]int, 1500001)

	MAX := 100000000

	//MAX = 101

	ans := 0

    for m := 1; m*m*2 <= MAX*2/3 ; m ++ {
    	for n := 1; n < m; n ++ {
    		if gcd(m,n) != 1 || ((m-n)%2) != 1 {
    			continue
    		}
    		a := m*m - n*n
    		b := 2*m*n
    		c := m*m + n*n

    		//c will always be max
    		//but a might be bigger than b

    		if c % diff(a, b) != 0 {
    			continue
    		}

    		fmt.Println(a, b, c)

    		if a + b + c < MAX {
    			ans += MAX/(a+b+c)
    		}
    	}
    }

	fmt.Println(ans)
}