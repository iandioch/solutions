package main

import (
	"fmt"
)

func diff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func main() {
	bestDiff := 2000000
	bestCount := 0
	bestW := 0
	bestH := 0
	for w := 1; w < 150; w ++ {
		for h := w+1; h < 150; h ++ {
			count := 0

			for i := 1; i <= w; i ++ {
				numAcross := w - i + 1
				for j := 1; j <= h; j ++ {
					numUp := h - j + 1

					num := numAcross * numUp
					count += num
				}
			}

			if diff(count, 2000000) < bestDiff {
				bestDiff = diff(count, 2000000)
				bestCount = count
				bestW = w
				bestH = h
				fmt.Println("w", w, "h", h, "n", count)
			}
		}
	}

	fmt.Println(bestCount, bestW*bestH)
}