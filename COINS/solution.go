package main

import (
	. "fmt"
)

func main() {
	var n int
	var err error
	for {
		if _, err = Scanln(&n); err != nil {
			// EOF
			break
		}
		Println(getMax(n))
	}
}

func mrdka() map[int]int {
	var m = make(map[int]int)
	m[0] = 0
	m[1] = 1
	m[2] = 2
	return m
}

var max = mrdka()

func getMax(n int) int {
	if val, ok := max[n]; ok {
		return val
	}

	sum := getMax(n/2) + getMax(n/3) + getMax(n/4)
	if sum > n {
		max[n] = sum
		return sum
	} else {
		max[n] = n
		return n
	}
}
