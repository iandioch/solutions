package main

import (
	"fmt"
	"./permute" // also used in #32
	"sort"
)

func main() {

	/*
	*	There's a smart way to do this, stepping through the nums one by one and figuring it out, but this is much easier
	*/
	perms := permute.Bytes([]byte("0123456789"))

	permStrings := make([]string, len(perms))

	for i := range perms {
		permStrings[i] = string(perms[i])
	}

	sort.Strings(permStrings)

	fmt.Println(permStrings[999999])
}