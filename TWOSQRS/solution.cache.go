package main

import (
	"bufio"
	. "fmt"
	"math"
	"os"
	"strconv"
	str "strings"
)

func main() {
	bio := bufio.NewReader(os.Stdin)
	firstLine := true
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
		n, _ := strconv.ParseFloat(str.TrimSpace(line), 64)
		Printf(solve(n) + "\n")
	}
}

var cache = make(map[float64]string)

func solve(n float64) string {
	if val, ok := cache[n]; ok {
		return val
	}

	max := math.Floor(math.Sqrt(n))

	for i := 0.0; i <= max; i++ {
		remainder := math.Sqrt(n - i*i)
		if remainder == math.Floor(remainder) {
			cache[n] = "Yes"
			return cache[n]
		}
	}

	cache[n] = "No"
	return cache[n]
}
