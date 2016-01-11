package main

import (
	"fmt"
)

func main() {
	ans := 0
	bound := int64(1073741824)

	// see this article https://plus.maths.org/content/play-win-nim

	for n := int64(1); n <= bound; n ++ {
		if n ^ (n*2) ^ (n*3) == 0 {
			ans ++
		}
	}

	fmt.Println(ans)
}