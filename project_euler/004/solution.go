package main

import (
	"fmt"
	"strconv"
)

func isPal(s string) bool{
	for i := range s {
		if s[i] != s[len(s) - 1 - i] {
			return false
		}
	}
	return true
}

func max (a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main (){
	maxn := 0
	for x := 100; x < 1000; x ++ {
		for y := 100; y < 1000; y ++ {
			str := strconv.Itoa(x*y)
			if isPal(str) {
				maxn = max(x*y, maxn)
			}
		}
	}

	fmt.Println(maxn)
}