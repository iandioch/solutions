package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(s string) bool {
	for i:= 0; i <= len(s)/2; i ++ {
		if s[i] != s[len(s)-i-1] {
			return false
		}
	}
	return true
}

func reverse(s string) string {
	r := ""
	for _, c := range s {
		r = string(c) + r
	}
	return r
}

func isLychrelNumber(n int) bool {
	s := strconv.Itoa(n)
	a, _ := strconv.Atoi(s)
	b, _ := strconv.Atoi(reverse(s))
	s = strconv.Itoa(a + b)
	for i := 1; i <= 50; i ++ {
		if isPalindrome(s) {
			return false
		}
		a, _ = strconv.Atoi(s)
		b, _ = strconv.Atoi(reverse(s))
		s = strconv.Itoa(a + b)
	}
	return true
}

func main() {
	numLychrel := 0
	for i := 196; i < 10000; i ++ {
		if isLychrelNumber(i) {
			//fmt.Println(i)
			numLychrel ++
		}
	}
	fmt.Println(numLychrel)
}