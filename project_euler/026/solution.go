// prob 26

package main

import (
	"fmt"
	//"strconv"
	"math/big"
)

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func getRepeat(numStr string) int {

	if len(numStr) < 2 {
		return 0
	}

	numStr = numStr[2:]

	repeats := []int{}
	for r := len(numStr)/2; r > 1; r -- {
		l := r
		if r + r > len(numStr) - 1 { 
			l = r + r - len(numStr)
		}

		if numStr[0:l] == numStr[r:r+l] {
			repeats = append(repeats, r)
		}
	}
	if len(repeats) > 0 { 
		return repeats[len(repeats)-1]
	}

	return 0
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

func main() {
	max := 1
	maxi := 2

	primes := getPrimes(1000)

	const prec = 10000
	ONE := new(big.Float).SetPrec(prec).SetInt64(1)
	for _, i := range primes {
		t := new(big.Float).SetPrec(prec).Quo(ONE, new(big.Float).SetPrec(prec).SetInt64(int64(i)))

		val := getRepeat(fmt.Sprintf("%.10000f\n", t))
		if val >= max {
			max = val
			maxi = i
		}
	}

	fmt.Println("answer =", maxi, "with recurring decimal of length", max)
}