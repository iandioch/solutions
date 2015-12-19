package main 

import (
	"fmt"
	"os"
	"bufio"
	"regexp"
	"strconv"
)

func min (a, b int) int {
	if a < b {
		return a
	}
	return b
}

func readLines(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan(){
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func main() {
	lines, _ := readLines("matrix.txt")
	nums := [][]int{}
	regex := regexp.MustCompile(",")

	for y := 0; y < len(lines); y ++ {
		l := []int{}
		parts := regex.Split(lines[y],-1)
		for x := 0; x < len(parts); x ++ {
			num, _ := strconv.Atoi(parts[x])
			l = append(l, num)
		}
		nums = append(nums, l)
	}

	for x := 1; x < len(nums[0]); x ++ {
		nums[0][x] = nums[0][x] + nums[0][x-1]
	}

	fmt.Printf("%v\n", nums[0])

	for y := 1; y < len(nums); y ++ {
		nums[y][0] = nums[y][0] + nums[y-1][0]

		fmt.Printf("%v\n", nums[y])
	}

	fmt.Printf("%v, %v\n", len(nums), len(nums[0]))

	for y := 1; y < len(nums); y ++ {
		for x := 1; x < len(nums[0]); x ++ {
			nums[y][x] = nums[y][x] + min(nums[y][x-1], nums[y-1][x])
		}
	}

	fmt.Printf("%d\n", nums[len(nums)-1][len(nums[0]) - 1])
}
