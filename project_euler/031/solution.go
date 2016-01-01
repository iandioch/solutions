package main

import (
	"fmt"
)

// get the num of ways to sum coins s[0] to s[m-1] coins to get sum of n
// learned from here: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
func count(s []int, m, n int) int {
	if n == 0 {
		//adds up exactly, nice
		return 1
	}
	if n < 0 {
		//doesn't add up exactly, doesn't work with this combo
		return 0
	}
	if m <= 0 && n >= 1 {
		//there's still some left of N we didn't reach but we're out of coins
		return 0
	}
	// count the ways by not including this coin, and by including this coin
	return count(s, m-1, n) + count(s, m, n - s[m-1])
}

func main() {
	s := []int{1, 2, 5, 10, 20, 50, 100, 200}

	fmt.Println(count(s, len(s), 200))
}