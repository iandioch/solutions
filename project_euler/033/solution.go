package main

import (
	"fmt"
	"math"
)

func floatEq(a, b float64) bool {
	return math.Abs(a-b) < 0.0000000001
}

func main () {
	for n1 := 1; n1 <= 9; n1 ++ { // first digit of numerator
		for n2 := 0; n2 <= 9; n2 ++ { // second digit of numerator
			for d1 := n1; d1 <= 9; d1 ++ { // first digit of denominator
				for d2 := 0; d2 <= 9; d2 ++ { // second digit of denominator
					if d2 != n1 && d1 != n2 {
						continue
					}
					numerator := n1*10 + n2
					denominator := d1*10 + d2
					if numerator > denominator {
						break
					}
					r := float64(numerator)/float64(denominator)
					a := float64(n1)/float64(d2)
					b := float64(n2)/float64(d1)

					if floatEq(a,b) {
						continue
					}

					if floatEq(r, a) {
						fmt.Println("a", numerator,"/",denominator, "=", n1,"/",d2,"=",a,r) //only this one is needed
					}
					if floatEq(r, b) {
						fmt.Println("b", numerator,"/",denominator, "=", n1,"/",d2,"=",a,r)
					}
				}
			}
		}
	}
}