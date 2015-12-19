// starting at the bottom of the triangle, find the max of each pair of elements in a row, and for each element in the next row sum that element with the max of the lower elements, and continue up the triangle like that

package main 

import (
	"fmt"
	"os"
	"bufio"
	"regexp"
	"strconv"
)

func max (a, b int) int {
	if a > b {
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
	lines, _ := readLines("triangle.txt")
	nums := [][]int{}
	regex := regexp.MustCompile("\\s+")
	for y := 0; y < len(lines); y ++ {
		parts := regex.Split(lines[len(lines) - y - 1], -1)
		row := []int{}
		for x := 0; x < len(parts); x ++ {
			num, _ := strconv.Atoi(parts[x])
			row = append(row, num)
		}
		nums = append(nums, row)
	}

	fmt.Printf("%v", nums)

	for y := 1; y < len(nums); y ++ {
		for index, elem := range(nums[y]) {
			nums[y][index] = elem + max(nums[y-1][index], nums[y-1][index+1])
		}
		fmt.Println(y)
	}

	fmt.Printf("%v", nums)

	fmt.Printf("%d\n", nums[len(nums)-1][0])
}
