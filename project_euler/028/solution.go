package main

import (
	"fmt"
)

func main() {
	total := 1
	curr := 1
	for length := 3; length <= 1001; length += 2 {
		for side := 1; side <= 4; side ++ {
			curr += (length-1)
			total += curr
			//fmt.Println(curr)
		}
	}
	fmt.Println("total", total)
}