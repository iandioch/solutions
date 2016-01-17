/*
*	Go implementation of Euler's product formula to find for the totient function (aka. phi function)
*	https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
*/

package main 

import (
	"fmt"
)

func getPrimeFactors(n int, primes []int) map[int]int {
	primeFacts := make(map[int]int) // keeps track of prime factor : exponent pairs
	for n != 1 {
		for i := 0; i < len(primes); i ++ {
			if n % primes[i] == 0 {
				val, ok := primeFacts[primes[i]]
				if !ok {
					val = 0
				}
				primeFacts[primes[i]] = val + 1
				n = n/primes[i]
				break
			}
		}
	}
	return primeFacts
}

func getPrimes(N int) []int {
	isComposite := make([]bool, N)
	primes := []int{}
	for i := 2; i < N; i ++ {
		if !isComposite[i] {
			primes = append(primes, i)
			for x := i+i; x < N; x += i {
				isComposite[x] = true
			}
		}
	}
	return primes
}

func totient(n int, primes []int) int {
	primeFacts := getPrimeFactors(n, primes)

	ans := n

	for prime := range primeFacts {
		ans = ans*(prime-1)/prime
	}
	return ans
}

func main(){
	primes := getPrimes(1000001)

	maxn := 0
	max := float64(0.0)

	for n := 2; n <= 1000000; n ++ {
		tot := totient(n, primes)
		result := float64(n)/float64(tot)
		if result > max {
			max = result
			maxn = n
			fmt.Println(maxn, max)
		}
	}

	fmt.Println(maxn)

	// the result is 510510, which is the product of the first 7 primes
}