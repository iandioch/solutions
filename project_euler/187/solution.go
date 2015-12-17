package main 

import (
	"fmt"
)

func getPrimes(n int) []int {
	//sieve of eratosthenes
	p := make([]bool, n)

	for i := 0; i < n; i ++ {
		p[i] = false
	}

	primes := []int{}

	for i := 2; i < n; i ++ {
		if !p[i] {
			primes = append(primes, i)
		}

		for j := i+i; j < n; j += i {
			p[j] = true
		}
	}
	return primes
}

func main(){
	primes := getPrimes(50000001)

	//fmt.Println(primes)

	fmt.Printf("%v primes\n", len(primes))

	num := 0

	for i := 0; i < len(primes); i ++ {
		for j := i; j < len(primes); j ++ {
			if primes[i]*primes[j] < 100000000 {
				//fmt.Println(primes[i]*primes[j])
				num ++
			}else{
				break
			}
		}
	}

	fmt.Println(num)
