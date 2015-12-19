package main

import ("fmt"; "strconv")

func main() {
	result := 1
	strLength := 0

	indexes := []int{1,10,100,1000,10000,100000,1000000}

	minIndex := 0
	for i := 1; i < 1000001; i ++ {
		numStr := strconv.Itoa(i) // cannot do string(int), as that takes ints as char values

		numStrLength := len([]rune(numStr))

		strLength += numStrLength

		for j := minIndex; j < len(indexes); j ++ {
			desIndex := indexes[j] - 1 // the zero-indexed desired element

			if desIndex < strLength {
				strIndex := desIndex - strLength + numStrLength
				num, _ := strconv.Atoi(string([]rune(numStr)[strIndex]))
				fmt.Printf("found index %d at num %s position %d (ie. %d)\n", indexes[j], numStr, strIndex, num)
				result *= num
				minIndex ++ // no need to keep iterating over this element of indexes[] from now on
			}
		}
	}

	fmt.Printf("%d\n", result)
}
