package main

import (
	"fmt"
)

func main(){
	numDivisors := make([]int, 10000000)

	for i := 2; i < len(numDivisors); i ++ {
		for j := i+i; j < len(numDivisors); j += i {
			numDivisors[j] ++
		}
	}

	ans := 0

	for n := 2; n < len(numDivisors) - 1; n ++ {
		if numDivisors[n] == numDivisors[n+1] {
			ans ++
		}
	}

	fmt.Println(ans) 
}