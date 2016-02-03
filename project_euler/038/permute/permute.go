// to use these functions, place this file in ./permute/permute.go and import "./permute"
// uses the "recursive algorithm" method from here: http://www.cut-the-knot.org/do_you_know/AllPerm.shtml
package permute

var level int
var value []int
var N int
var num int
var intPerms [][]int
var bytePerms [][]byte

func visitInt(k int, input []int) {
	level += 1
	value[k] = level
	if level == N {
		num ++
		arr := make([]int, len(value))
		for i, v := range value {
			arr[i] = input[v-1]
		}
		intPerms = append(intPerms, arr)
	}else {
		for i := 0; i < N; i ++ {
			if value[i] == 0 {
				visitInt(i,input)
			}
		}
	}
	level --
	value[k] = 0
}

func visitByte(k int, input []byte) {
	level += 1
	value[k] = level
	if level == N {
		num ++
		arr := make([]byte, len(value))
		for i, v := range value {
			arr[i] = input[v-1]
		}
		bytePerms = append(bytePerms, arr)
	}else {
		for i := 0; i < N; i ++ {
			if value[i] == 0 {
				visitByte(i,input)
			}
		}
	}
	level --
	value[k] = 0
}

func Ints(in []int) [][]int{
	value = make([]int, len(in))
	for i := range value {
		value[i] = 0
	}
	intPerms = [][]int{}
	N = len(in)
	level = -1
	num = 0
	visitInt(0,in)
	return intPerms
}

func Bytes(in []byte) [][]byte {
	value = make([]int, len(in))
	for i := range value {
		value[i] = 0
	}
	bytePerms = [][]byte{}
	N = len(in)
	level = -1
	num = 0
	visitByte(0,in)
	return bytePerms
}