package main

import (
	"fmt"
	"os"
	"bufio"
)

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

	//lines, _ = readLines("test.txt")

	ans := 0

	for _, line := range lines {
		origLength := len(line)
		newLength := len(line) + 2
		for i := 0; i < len(line); i ++ {
			if line[i] == '"' || line[i] == '\\' {
				//fmt.Print("\\")
				newLength ++
			}
			//fmt.Print(string(line[i]))
		}

		//fmt.Println()

		ans += newLength - origLength
		//fmt.Println(line, origLength, newLength)
	}

	fmt.Println(ans)
}