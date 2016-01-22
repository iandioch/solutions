package main

import (
	"fmt"
)

func count(n int) int {
	nums := []string{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	teenNums := []string{"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	tenNums := []string{"", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}

	units := n % 10
	tens := (n/10) % 10
	hundreds := (n/100) % 10
	thousands := 0
	if n == 1000 {
		thousands = 1
	}

	ans := ""
	if tens == 1 {
		if units == 0 {
			ans += "ten"
		}else{
			ans += teenNums[units]
		}
	}else if tens == 0 {
		ans += nums[units]
	}else {
		ans = ans + tenNums[tens] + nums[units]
	}
	if hundreds != 0 {
		if units != 0 || tens != 0 {
			ans = nums[hundreds] + "hundredand" + ans
		}else{
			ans = nums[hundreds] + "hundred"
		}
	}
	if thousands != 0 {
		if hundreds != 0 || tens != 0 || units != 0 {
			ans = "onethousandand" + ans
		}else{
			ans = "onethousand" + ans
		}
	}

	fmt.Println(n, ans)
	return len(ans)

}

func main() {
	ans := 0
	for i := 1; i <= 1000; i ++ {
		ans += count(i)
	}
	fmt.Println(ans)
}