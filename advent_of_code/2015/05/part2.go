package main

import (
	"fmt"
	"os"
	"bufio"
)

func isNice(s string) bool {
	foundDouble := false

	for i := 0; i < len(s) - 3; i ++ {
		t := s[i:i+2]
		for j := i + 2; j < len(s) - 1; j ++{
			if t == s[j:j+2] {
				foundDouble = true
			}
		}
	}

	foundRepeat := false

	for i := 0; i < len(s) - 2; i ++ {
		if s[i] == s[i+2] {
			foundRepeat = true
		}
	}

	return foundDouble && foundRepeat
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

	//lines = []string{"qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"}

	numNice := 0

	for _, line := range lines {
		if isNice(line) {
			numNice ++
		}
	}

	fmt.Println(numNice)
}