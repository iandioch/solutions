package main

import (
	"fmt"
	"./permute"
)

func tryPerm(order []int) map[int]bool {
	nums := make(map[int]bool)
	xi := 0
	for a := 1; a < len(order)-4; a ++ {
		xi = xi*10 + order[a-1]

		yi := order[a]

		for b := a+1; b < len(order) - 3; b ++ {
			yi = yi*10 + order[b]
			zi := 0
			for c := b+1; c < len(order); c ++ {
				zi = zi*10 + order[c]
			}

			if xi*yi == zi {
				fmt.Println(xi,"*",yi,"=",zi)
				nums[zi] = true
			}
		}
	}
	return nums
}

func main() {
	combos := permute.Ints([]int{1,2,3,4,5,6,7,8,9})

	nums := make(map[int]bool)

	for _, v := range combos {
		for i, _ := range tryPerm(v) {
			nums[i] = true
		}
	}

	sum := 0
	for i, _ := range nums {
		sum += i
	}

	fmt.Println(sum)
}