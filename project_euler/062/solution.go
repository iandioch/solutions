package main

import (
	"fmt"
	"sort"
	"strings"
	"strconv"
)

func sortString(s string) string {
	c := strings.Split(s, "")
	sort.Strings(c)
	return strings.Join(c, "")
}
func main(){
	cubeDigits := make(map[string][]uint64)
	var n uint64 = 200
	for n < 10000 {
		n3 := n*n*n
		sorted := strconv.FormatUint(n3, 10)
		sorted = sortString(sorted)
		//fmt.Println(n, n3, sorted)
		l, ok := cubeDigits[sorted]
		if ok{
			cubeDigits[sorted] = append(l, n3)
		}else{
			cubeDigits[sorted] = []uint64{n3}
		}
		n ++
	}
	answers := []uint64{}
	for _, j := range cubeDigits{
		if len(j) == 5 {
			//fmt.Println(j)
			for _, k := range j {
				answers = append(answers, k)
			}
			//answers = append(answers, j[:])
		}
	}
	var min uint64 = (2 << 63)-1
	for _, j := range answers{
		if j < min {
			min = j
		}
	}
	fmt.Println(min)
}
