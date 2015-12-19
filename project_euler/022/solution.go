package main

import (
	"fmt"
	"os"
	"bufio"
	"sort"
	"regexp"
)

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

func getVal(s string) int {
	total := 0
	for _, runeValue := range s {
		if runeValue == 34 {
			continue
		}
		val := int(runeValue - 64)
		total += val
	}
	return total
}

func main() {
	lines, err := readLines("names.txt")

	if err != nil {
		fmt.Println(err)
		return
	}

	regex := regexp.MustCompile(",")
	names := regex.Split(lines[0], -1)

	sort.Strings(names)

	total := 0

	for i := 0; i < len(names); i ++ {
		val := getVal(names[i])
		total += val*(i+1)
	}


	fmt.Println(total)
}
