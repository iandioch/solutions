/*
*	Go implementation of Euler's product formula to find for the totient function (aka. phi function)
*	https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
*/

package main 

import (
	"fmt"
	"strconv"
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

func countChars(a string) map[rune]int {
	result := make(map[rune]int)
	for i := '0'; i <= '9'; i ++ {
		result[i] = 0
	}
	const ZERO rune = '0'
	for _, c := range a {
		result[c - ZERO] ++
	}
	return result
}

func isPerm(a, b string) bool {
	x := countChars(a)
	y := countChars(b)

	if(len(x) != len(y)){
		return false
	}

	for i := range x {
		if x[i] != y[i] {
			return false
		}
	}
	return true
}

func main(){
	primes := getPrimes(10000)

	minn := 1000000000
	min := float64(10000000.0)

	for _, a := range primes {
		if a < 1000 || a > 9000 {
			continue
		}
		for _, b := range primes {
			if b < 1000 || b > 9000 {
				continue
			}
			n := a*b
			if n >= 10000000 {
				break
			}

			tot := totient(n, primes)

			if !isPerm(strconv.Itoa(n), strconv.Itoa(tot)) {
				continue
			}
			result := float64(n)/float64(tot)
			if result < min {
				min = result
				minn = n
				//fmt.Println(minn, min)
			}
		}
	}

	fmt.Println("primes crunched")

	/*for n := 10000000 - 1; n >= 1; n -- {
		tot := totient(n, primes)
		if !isPerm(strconv.Itoa(n), strconv.Itoa(tot)) {
			continue
		}
		result := float64(n)/float64(tot)
		if result < min {
			min = result
			minn = n
			fmt.Println(minn, min)
		}
	}*/

	fmt.Println(minn)

	// the result is 510510, which is the product of the first 7 primes
}