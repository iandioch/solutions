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
		repLength := len(line)
		trueLength := 0
		for i := 1; i < len(line) - 1; i ++ {
			//fmt.Printf("%c", line[i])
			trueLength ++
			if line[i] == '\\' {
				if line[i + 1] == '\\' {
					i ++;
					continue;
				}
				if line[i + 1] == '"' {
					i ++;
					continue;
				}
				if line[i + 1] == 'x' {
					i += 3
					continue
				}
			}
		}
		//fmt.Println("\n", line, repLength, trueLength)
		ans += repLength - trueLength
	}

	fmt.Println(ans)
}