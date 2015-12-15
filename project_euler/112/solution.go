package main

import (
	"fmt"
	"strconv"
)

func isRising(numStr string) bool {
	for k, v := range(numStr) {
		if k == 0{
			continue
		}
		if int(v) < int(numStr[k-1]) {
			//fmt.Printf("%v : %c < %c\n", k,  v, numStr[k-1])
			return false
		}
	}
	return true
}

func isFalling(numStr string) bool {
	for k, v := range(numStr) {
		if k == 0{
			continue
		}
		if int(v) > int(numStr[k-1]) {
			//fmt.Printf("%v : %c > %c\n", k,  v, numStr[k-1])
			return false
		}
	}
	return true
}

func isBouncy(num int) bool {
	numStr := strconv.Itoa(num)
	//fmt.Println(num, numStr)
	return !(isRising(numStr) || isFalling(numStr))
}

func main() {
	numBouncy := []int{0}

	ratio := 0

	var index int = 0

	for ratio != 99 {
		index ++
		num := numBouncy[len(numBouncy) - 1]
		if isBouncy(index) {
			//fmt.Println("bouncy!")
			num ++
		}
		numBouncy = append(numBouncy, num)
		//fmt.Printf("%v\n", numBouncy)
		ratio = (100*num)/index
	}
	//fmt.Println(maxNum)
	fmt.Printf("%v\n", index)
}
