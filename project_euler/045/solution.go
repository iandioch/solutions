// problem 45
package main

import (
	"fmt"
)

type triAndPent struct {
	x, y, num int
}

func main() {

	const MAX_VAL int = 100000

	tps := []triAndPent{}

	minY := 165

	for x := 285; x < MAX_VAL; x ++ {
		for y := minY; y < x; y ++ {
			if x*(x+1) == y*(3*y - 1) {

				num := (x*(x+1))/2
				tps = append(tps, triAndPent{x, y, num})

				minY = y

				fmt.Println("found one that is triangle & petagonal", x, y, num)
			}
		}
	}

	hexNums := make(map[int]bool)

	for n := 1; n < MAX_VAL; n ++ {
		hexNums[n*(2*n - 1)] = true
	}

	fmt.Printf("%v\n", tps)

	for _, el := range (tps) {

		_, isHex := hexNums[el.num]
		if isHex {
			fmt.Println("found tri, pent & hex:", el.num)
		}
	}
}
