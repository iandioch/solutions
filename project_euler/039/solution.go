package main

import (
	"fmt"
	"math"
)

func main() {
	var vals [1001]int

	for a := 1; a < len(vals) - 2; a ++ {
		for b := a; a + b < len(vals) - 1; b ++ {
			c := int(math.Floor(math.Sqrt(float64(a*a + b*b))))

			if a*a + b*b == c*c && a+b+c < len(vals) {
				vals[a+b+c] += 1
			}
		}
	}

	max := 0
	maxi := 0

	for i, v := range vals {
		//fmt.Println(i, v)
		if v > max {
			maxi = i
			max = v
		}
	}

	fmt.Println(maxi, max)

}
