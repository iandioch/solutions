package main

import (
	"fmt"
	"strconv"
)

func countChars(n int) map[rune]int {
	s := strconv.Itoa(n)
	r := make(map[rune]int)
	for _, c := range s {
		_, ok := r[c]
		if !ok {
			r[c] = 1
		}else{
			r[c] += 1
		}
	}
	return r
}

func mapEq(a, b map[rune]int) bool{
	if len(a) != len(b) {
		return false
	}

	for i, _ := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func main() {
	for i := 1; i < 1 << 31 - 1; i ++ {
		digits := countChars(i)
		found := true
		for k := i + i; k <= i*6; k += i {
			if !mapEq(digits, countChars(k)) {
				found = false
				break
			}
		}
		if found {
			fmt.Println(i)
			return
		}
	}
}