package main

import (
	"fmt"
	"strconv"
)

func isPal(s string) bool {
	for i := 0; i < len(s)/2; i ++ {
		if s[i] != s[len(s) - i - 1] {
			return false
		}
	}
	return true
}

func isDouble(a int) bool {
	return isPal(strconv.Itoa(a)) && isPal(strconv.FormatInt(int64(a), 2))
}

func main() {
	sum := 0
	for i := 1; i < 1000000; i += 2 {
		if isDouble(i) {
			sum += i
			//fmt.Println(i)
		}
	}
	fmt.Println("sum", sum)
}