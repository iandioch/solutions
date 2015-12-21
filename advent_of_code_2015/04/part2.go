package main

import (
	"fmt"
	"crypto/md5"
	//"encoding/hex"
	"strconv"
)

func main() {

	key := "yzbqklnj"
	for i := 1; ; i ++ {
		k := key + strconv.Itoa(i)

		hexa := fmt.Sprintf("%x", md5.Sum([]byte(k)))

		if hexa[0:6] == "000000" {
			fmt.Println(i, hexa)
			return
		}
	}
}