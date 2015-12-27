package main

import (
	"fmt"
	"strconv"
)

func isPrime(n int, primeSet map[int]bool) bool {
	_, ok := primeSet[n]
	return ok
}

func getPrimes(N int) []int {
	isComposite := make([]bool, N)
	primes := []int{}
	for i := 2; i < N; i ++ {
		if !isComposite[i] {
			primes = append(primes, i)

			for j := i+i; j < N; j += i {
				isComposite[j] = true
			}
		}
	}
	return primes
}

func main() {
	primes := getPrimes(10000000)

	primeSet := make(map[int]bool)
	for _, p := range primes {
		primeSet[p] = true
	}

	tested := make(map[int]bool)
	ans := 0

	for i := 2; i < 1000000; i ++ {
		_, ok := tested[i]
		if ok {
			continue
		}
		s := strconv.Itoa(i)
		circular := true

		count := 0
		for j := 0; j < len(s); j ++ { // offset
			t := s[j+1:] + s[0:j+1]

			num, _ := strconv.Atoi(t)

			if !isPrime(num, primeSet) {
				circular = false
				break
			}

			if !tested[num] {
				count ++
			}

			tested[num] = true
		}

		if circular {
			ans += count
		}
	}

	fmt.Println(ans)
}