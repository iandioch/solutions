package main

import (
	"fmt"
)

func main() {

	MAX := int64(100000000)

	isComposite := make([]bool, MAX)
	primeSet := make(map[int64]bool)

	for i := int64(2); i < MAX; i ++ {
		if !isComposite[i] {
			primeSet[int64(i)] = true
			for j := i + i; j < MAX; j += i {
				isComposite[j] = true
			}
		}
	}

	sum := int64(0)

	// only need to check numbers that are one less than a prime, as the first test will be 1 + N.
	for k, _ := range primeSet {
		n := int64(k - 1)

		valid := true

		for i := int64(1); i*i <= n; i ++ {
			if n % i != 0 {
				continue
			}
			j := n/i

			s := i + j
			_, ok := primeSet[s]
			if !ok {
				valid = false
				break
			}			
		}

		if valid {
			sum += n
		}
	}

	fmt.Println("sum", sum)
}