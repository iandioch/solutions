//problem 23

package main

import (
	"fmt"
)

func getSumOfDivisors(n int) int {
	sum := 1
	for i := 2; i*i <= n; i ++ {
		if n % i == 0 {
			sum += i
			if i*i != n{
				sum += n/i
			}
		}
	}
	return sum
}

func main() {
	abundants := []int{}

	for i := 2; i < 28123; i ++ {
		if getSumOfDivisors(i) > i {
			abundants = append(abundants, i)
		}
	}

	canBeSum := make(map[int]bool)

	for _, m := range(abundants){
		for _, n := range(abundants){
			canBeSum[m+n]=true
		}
	}

	sum := 0

	for i := 1; i < 28123; i ++ {
		_, found := canBeSum[i]

		if !found {
			sum += i
		}
	}

	fmt.Println("total", sum)
}