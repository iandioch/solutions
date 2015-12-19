// project euler #19
// it felt like cheating to use a datetime library

package main

import (
	"fmt"
)

func main(){
	day := 1

	monthLengths := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

	ans := 0

	for year := 1900; year < 2001; year ++ {

		leapYear := false

		if (year % 400 == 0) || (year % 100 != 0 && year % 4 == 0) {
			leapYear = true
		}

		dayOfYear := 1
		for monthIndex, monthLength := range monthLengths {
			if monthIndex == 1 && leapYear {
				monthLength ++
			}

			if year > 1900 && day % 7 == 0 {
				fmt.Println("found one: ", day, year, dayOfYear, monthIndex)
				ans ++
			}

			dayOfYear += monthLength
			day += monthLength
		}

		//fmt.Println(year, dayOfYear)
	}

	fmt.Println(ans)
}
