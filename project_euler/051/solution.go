package main

import (
	"fmt"
	"strconv"
	"strings"
)

func getPrimes(n int) []int {
	primes := []int{}
	isComposite := make([]bool, n)

	for i := 2; i < n; i ++ {
		if !isComposite[i] {
			primes = append(primes, i)
			for j := i+i; j < n; j += i {
				isComposite[j] = true
			}
		}
	}

	return primes
}

func indexesOf(s, sep string) []int {
	r := []int{}
	for i := 0; i  + len(sep) <= len(s); i ++ {
		if s[i:i+len(sep)] == sep {
			r = append(r, i)
		}
	}
	return r
}

//used in getPermutations. Get all permutations of the string s by replacing occurances of currNum with a *
func p(currNum string, s string) []string{
	if len(s) == 0 {
		return []string{""}
	}
	r := []string{s}

	for _, v := range indexesOf(s, currNum) {
		base := s[0:v]

		for _, w := range p(currNum, s[v+1:]) {
			r = append(r, base + "*" + w)
		}
	}

	return r
}

// get all permutations of the string s with each digit in strs replaced by a *
func getPermutations(strs []string, s string) []string {
	r := []string{}
	for _, num := range strs {
		for _, v := range p(num, s) {
			//check if they are not equal, as if they are, nothing has been replaced; there are no * in the result
			if v != s {
				r = append(r, v)
			}
		}
	}
	return r
}

func main(){
	// keep a map of every string with replaced digits (eg "*3") and figure out how many primes that can apply to
	primes := getPrimes(1000000)
	strs := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
	numPrimes := make(map[string]int)

	for _, prime := range primes {
		s := strconv.Itoa(prime)

		// get all possible digit replacements for this prime
		ns := getPermutations(strs, s)
		for _, n := range ns {

			//add one to the count of this string
			_, ok := numPrimes[n]
			if ok {
				numPrimes[n] += 1
			}else{
				numPrimes[n] = 1
			}
		}
	}

	for k, v := range numPrimes {
		if v == 8 {
			fmt.Println(k)

			for _, w := range strs {
				s := strings.Replace(k, "*", w, -1)
				n, _ := strconv.Atoi(s)

				//check if it is prime
				for _, p := range primes {
					if p == n {
						fmt.Println(p)
						return
					}
				}
			}
		}
	}
}