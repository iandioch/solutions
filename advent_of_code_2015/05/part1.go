package main

import (
	"fmt"
	"os"
	"bufio"
)

func isNice(s string) bool {
	numVowels := 0
	foundDouble := false
	for i := 0; i < len(s); i ++ {
		if s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' {
			numVowels ++
		}

		if i == len(s) - 1 {
			break
		}

		if s[i] == s[i+1] {
			foundDouble = true
		}

		if (s[i] == 'a' && s[i+1] == 'b') || (s[i] == 'c' && s[i+1] == 'd') || (s[i] == 'p' && s[i+1] == 'q') || (s[i] == 'x' && s[i+1] == 'y') {
			return false
		}
	}

	//fmt.Println(s, numVowels, foundDouble)

	return numVowels >= 3 && foundDouble
}

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

	numNice := 0

	for _, line := range lines {
		if isNice(line) {
			numNice ++
		}
	}

	fmt.Println(numNice)
}