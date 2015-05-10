package main

import (
	"bufio"
	. "fmt"
	"math/big"
	"os"
	str "strings"
)

func main() {
	bio := bufio.NewReader(os.Stdin)
	firstLine := true
	a := big.NewInt(0)
	b := big.NewInt(0)
	for {
		line, err := bio.ReadString(0x0A)
		if err != nil {
			// EOF
			break
		}
		if firstLine {
			firstLine = false
			continue
		}
		nums := str.Fields(line)
		a.SetString(nums[0], 10)
		b.SetString(nums[1], 10)
		Printf("%v\n", a.Mul(a, b))
	}
}
