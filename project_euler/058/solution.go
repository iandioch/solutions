package main

import (
	"fmt"
	//"math"
)

func getPrimeSet(n int) (map[int]bool, int) {
	isComposite := make([]bool, n)
	primeSet := make(map[int]bool)
	maxPrime := 0

	for i := 2; i < n; i ++ {
		if !isComposite[i] {
			primeSet[i] = true
			maxPrime = i
			for j := i+i; j < n; j += i {
				isComposite[j] = true
			}
		}
	}
	return primeSet, maxPrime
}

func isPrime (primes map[int]bool, maxPrime, n int) bool{
	if n < maxPrime {
		_, ok := primes[n]
		return ok
	}else {
		for i := 2; i*i <= n; i ++ {
			if n % i == 0 {
				return false
			}
		}
	}
	return true
}

func main() {
	curr := 1

	numPrime := 0
	numNums := 1

	length := 3

	primes, maxPrime := getPrimeSet(20000000)
	for ; length <= 1000001; length += 2 {

		for side := 1; side <= 4; side ++ {
			curr += (length-1)
			numNums ++
			if side == 4 {
				//squares
			}else if isPrime(primes, maxPrime, curr) {
				numPrime ++
			}
		}
		if float64(numPrime)/float64(numNums) < 0.1 {
			fmt.Println(curr)
			fmt.Println("Found", length, numPrime, numNums, float64(numPrime)/float64(numNums))
			break
		}
	}
	fmt.Println("side length", length)
	fmt.Println("ratio", 100*float64(numPrime)/float64(numNums), "(", numPrime, "primes /", numNums, "numbers )")
}