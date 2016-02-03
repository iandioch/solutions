package main

import (
	"fmt"
	"strconv"
)

func getPrimes(n int) map[int]bool {
	isComposite := make([]bool, n)
	primes := make(map[int]bool)

	for i := 2; i < n; i ++ {
		if !isComposite[i] {
			primes[i] = true

			for j := i+i; j < n; j += i {
				isComposite[j] = true
			}
		}
	}
	return primes
}

func main(){
	primes := getPrimes(1000000)

	sum := 0

	for p := range primes {
		if p <= 7 {
			continue
		}
		s := strconv.Itoa(p)

		valid := true

		for l := 1; l < len(s); l ++ {
			a := s[l:]
			x, _ := strconv.Atoi(a)
			_, ok := primes[x]
			if !ok {
				valid = false
				break
			}

			a = s[0:len(s)-l]
			x,_ = strconv.Atoi(a)
			_, ok = primes[x]
			if !ok {
				valid = false
				break
			}
		}

		if valid {
			fmt.Println("->", s)
			sum += p
		}
	}
	fmt.Println(sum)
}