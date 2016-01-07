package main

import (
	"fmt"
	"os"
	"bufio"
)

func loadString(filePath string) (string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return "", err
	}
	defer file.Close()
	line := ""
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line += scanner.Text()
	}
	return line, scanner.Err()
}

func getValue(s string) int {
	val := 0
	for _, c := range s {
		val += int(c) - int('A') + 1
	}
	return val
}

func main() {

	// calculate the triangle numbers and put them in a set
	triangles := make(map[int]bool)
	for i := 1; i < 1000; i ++ {
		v := i*(i+1)/2
		triangles[v] = true
	}

	fmt.Println(triangles)

	// load the words
	line, err := loadString("words.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(getValue("SKY"))

	//parse the file to pick out the words
	word := ""
	num := 0
	for _, c := range line {
		if c == ',' {
			val := getValue(word)
			fmt.Println(word, val)

			// check if the word value appears in our map of triangle numbers
			_, ok := triangles[val]
			if ok {
				num ++
			}
			word = ""
		}else if c != '"' && c != ' ' {
			word += string(c)
		}
	}
	
	// there'll be one word left over as the file doesn't have a trailing comma
	val := getValue(word)
	_, ok := triangles[val]
	if ok {
		num ++
	}

	fmt.Println(num)
}