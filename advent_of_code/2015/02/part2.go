package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
	"strings"
)

func min2(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func min(a, b, c int) int {
	return min2(a, min2(b, c))
}

func sort(a, b, c int) (int, int, int) {
	if c < a {
		a, c = c, a
	}
	if b < a {
		a, b = b, a
	}
	if c < b {
		b, c = c, b
	}
	return a, b, c
}

// http://stackoverflow.com/questions/5884154/golang-read-text-file-into-string-array-and-write
func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	in := bufio.NewScanner(file)
	for in.Scan() {
		lines = append(lines, in.Text())
	}
	return lines, in.Err()
}

func main() {
	lines, _ := readLines("input.txt")

	//lines = []string{"2x3x4", "1x1x10"}

	total := 0

	for _, line := range lines {
		parts := strings.Split(line, "x")

		x,_ := strconv.Atoi(parts[0])
		y,_ := strconv.Atoi(parts[1])
		z,_ := strconv.Atoi(parts[2])

		a, b, c := sort(x, y, z)

		shortestDist := a+a+b+b
		cube := a*b*c

		total += shortestDist + cube

		fmt.Println(shortestDist + cube)

		//fmt.Println(req)
	}

	fmt.Println(total)
}