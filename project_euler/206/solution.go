// prob 206

package main

import (
	"fmt"
	"strconv"
	"math"
)

func isCorrectSquare(num int64) bool {
	bytes := []byte{}
	bytes = strconv.AppendInt(bytes, num, 10)
	s := string(bytes)
	return len(s) == 19 && s[0] == '1' && s[2] == '2' && s[4] == '3' && s[6] == '4' && s[8] == '5' && s[10] == '6' && s[12] == '7' && s[14] == '8' && s[16] == '9'
	// no need to check last num, as we are only trying multiples of 10
}

func main(){

	var MIN int = int(math.Sqrt(1020304050607080900))
	var MAX int = int(math.Sqrt(1929394959697989990))

	fmt.Println(MIN, MAX)
	for i := MIN; i <= MAX; i += 10 {
		// num ends in 0, so i must be a multiple of 10
		if isCorrectSquare(int64(i)*int64(i)){
			fmt.Println(i, i*)
			return
		}
	}
}