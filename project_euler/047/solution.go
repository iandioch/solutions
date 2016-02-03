// problem 47

package main

import (
	"fmt"
	"math"
)

func getPrimes(n int) []int {
	isNotPrime := make([]bool, n)
	primes := []int{}

	//primeSet := make(map[int]bool)

	for i := 2; i < n; i ++ {
		if !isNotPrime[i] {
			primes = append(primes, i)

			//primeSet[i] = true

			for j := i; j < n; j += i {
				isNotPrime[j] = true
			}
		}
	}

	return primes
}

// returns a structure mapping each prime factor to its exponent
// eg primeFactorSet(12, primes) returns map{2:2, 3:1}
func primeFactorSet(in int, primes []int) map[int]int {
	n := in
	ret := make(map[int]int)
	for i := 0; i < len(primes); i ++ {
		if n % primes[i] == 0 {
			//fmt.Println(n, primes[i])
			n = n / primes[i]
			_, ok := ret[primes[i]]
			if ok {
				ret[primes[i]] = ret[primes[i]] + 1
			}else {
				ret[primes[i]] = 1
			}
			i = -1
			if n == 1 {
				break
			}
		}
	}
	return ret
}

//returns a^b, slightly faster than using math.Pow as the nums don't need to be converted to float64s and back
func pow(a, b int) int{
	r := 1
	for i := 0; i < b; i ++ {
		r *= a
	}
	return r
}

func main() {
	MAXNUM := 500000 // arbitrarily high number, if too low, repeat the program with a higher num
	primes := getPrimes(int(math.Sqrt(float64(MAXNUM)))) // no need to get all the primes up to the number
	startingNum := 1000 // arbitrary low number, guessed (correctly) it was going to be > 1000 (by a fair bit)


	a, b, c, d := primeFactorSet(startingNum-1, primes), primeFactorSet(startingNum, primes), primeFactorSet(startingNum+1, primes), primeFactorSet(startingNum+2, primes)
	//would be expandable to any number, not just 4, if an array of length 4 was used here instead of hardcoded vars

	for i := startingNum; i < MAXNUM; i ++ {
		d = (c)
		c = (b)
		b = (a)

		a = primeFactorSet(i, primes)

		if len(d) != 4 || len(c) != 4 || len(b) != 4 || len(a) != 4 {
			continue
		}

		if i % 1000 == 0 {
			fmt.Println(i)
		}

		facts := make(map[int]bool)

		good := true


		for x := range a {
			r := pow(x, a[x])
			_, ok := facts[r]
			if ok {
				good = false
				break
			}
			facts[r] = true
		}
		if !good {
			continue
		}

		for x := range b {
			r := pow(x, b[x])
			_, ok := facts[r]
			if ok {
				good = false
				break
			}
			facts[r] = true
		}
		if !good {
			continue
		}

		for x := range c {
			r := pow(x, c[x])
			_, ok := facts[r]
			if ok {
				good = false
				break
			}
			facts[r] = true
		}
		if !good {
			continue
		}
		for x := range d {
			r := pow(x, d[x])
			_, ok := facts[r]
			if ok {
				good = false
				break
			}
			facts[r] = true
		}
		if !good {
			continue
		}

		//print out the first number in the run
		fmt.Println(i-3)
		break
	}
}