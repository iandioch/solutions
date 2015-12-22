package main 

import "fmt"

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a % b
	}
	return a
}

func main() {
	r := 1
	for i := 20; i > 1; i -- {
		if r % i != 0 {
			r *= i/gcd(r, i)
		}
	}
	fmt.Println(r)
}