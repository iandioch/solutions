package main 

import (
	"fmt"
	"math/big"
)

func nCr(n, r int, fact []big.Int) big.Int {
	return *big.NewInt(1).Div(&fact[n], big.NewInt(1).Mul(&fact[r], &fact[n-r]))
	//return fact[n]/(fact[r]*fact[n-r])
}

func main() {
	fact := []big.Int{}

	bi := big.NewInt(1)

	fact = append(fact, *bi)

	for i := 1; i <= 100; i ++ {
		bi = big.NewInt(int64(i))
		fact = append(fact, *bi.Mul(bi, &fact[len(fact)-1]))

		fmt.Println(fact[len(fact)-1].String())
		//fact = append(fact, int64(i)*fact[len(fact)-1])
	}

	//fmt.Println(fact)

	num := 0

	minR := 9

	bound := big.NewInt(1000000)

	for n := 23; n <= 100; n ++ {
		for r := minR; r <= n/2; r ++ {
			
			val := nCr(n, r, fact)
			fmt.Println(n, r, n-r, (val.String()))
			if val.Cmp(bound) < 0 {
				continue
			}
			fmt.Println(n, r, n-r, val.String(), "hit")
			if r == minR {
				minR -- // *****
			}
			if r == n - r {
				num ++
			}else{
				num += 2
			}
		}
	}

	fmt.Println(num)
}