package main

import (
	"fmt"
	"./permute"
	//"math"
	"strconv"
)

func getString(num int) string {
	str := strconv.Itoa(num)
	for x := 2; len(str) < 9; x ++ {
		str += strconv.Itoa(num*x)
	}
	return str
}

func main () {
	orders := permute.Bytes([]byte("123456789"))

	//fmt.Println(orders)

	maxn := 0
	ans := ""

	for _, order := range orders {
		orderString := string(order)
		
		num := int(order[0] - '0')

		if getString(num) == orderString {

		}

		for i := 1; i < 5; i ++ {
			num = num*10 + int(order[i] - '0')

			if getString(num) == orderString {
				fmt.Println(orderString)
				if num > maxn {
					maxn = num
					ans = orderString
				}
			}

		}
	}

	fmt.Println(ans)
}