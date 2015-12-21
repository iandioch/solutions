// problem 30
package main

import (
	"fmt"
	"strconv"
)

var digits map[rune]int = map[rune]int{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

func getVal(num int) int {
	numstr := strconv.Itoa(num)
	total := 0
	for _, c := range numstr {
		i := digits[c]
		total += i*i*i*i*i
	}
	return total
}

func isValid(num int) bool {
	return getVal(num) == num
}

func main() {
	total := 0

	for i := 2; i < 1000000; i ++ {
		//fmt.Println(i, getVal(i))
		if(isValid(i)){
			fmt.Println(i, total)
			total += i
		}
	}

	fmt.Println(total)
}