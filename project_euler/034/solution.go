package main

import (
	"fmt"
	"strconv"
)

func digitFactSum(n int) int{
	total := 0
	s := strconv.Itoa(n)
	//fmt.Println(n, n, s)
	for _, c := range s {
		if c == '0'{
			total += 1
		}else if c == '1' {
			total += 1
		}else if c == '2' {
			total += 2
		}else if c == '3' {
			total += 6
		}else if c == '4' {
			total += 24
		}else if c == '5' {
			total += 120
		}else if c == '6' {
			total += 720
		}else if c == '7' {
			total += 5040
		}else if c == '8' {
			total += 40320
		}else if c == '9' {
			total += 362880
		}
	}
	//fmt.Println(n, total)
	return total
}

func main() {
	n := 0
	for i := 10; i < 362880*7; i ++ {
		if digitFactSum(i) == i {
			n += i
			fmt.Println(i)
		}
	}
	fmt.Println(n)
}