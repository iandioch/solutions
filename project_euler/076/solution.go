package main

import (
	"fmt"
)

// get the num of ways to sum coins s[0] to s[m-1] coins to get sum of n
// learned from here: http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
// copied from problem 31, but with memoisation
func count(memo map[int]map[int]int, m, n int) int {
	v, ok := memo[m][n]

	if ok {
		return v
	}
	if n == 0 {
		//adds up exactly, nice
		return 1
	}
	if n < 0 {
		//doesn't add up exactly, doesn't work with this combo
		return 0
	}
	if m <= 0 && n > 0 {
		//there's still some left of N we didn't reach but we're out of coins
		return 0
	}
	// count the ways by not including this coin, and by including this coin
	memo[m][n] = count(memo, m-1, n) + count(memo, m, n - (m))
	return memo[m][n]
}

func main() {
	memo := make(map[int]map[int]int)
	for i := 0; i < 100; i ++ {
		memo[i] = make(map[int]int)
	}
	fmt.Println(count(memo, 99, 100))
}