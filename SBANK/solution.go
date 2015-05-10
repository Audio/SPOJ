package main

import (
	"bufio"
	. "fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var bio *bufio.Reader

func main() {
	bio = bufio.NewReader(os.Stdin)

	tasks, _ := strconv.ParseUint(getLine(), 10, 8)

	for tasks > 0 {
		accounts := make(map[string]uint32)

		lines, _ := strconv.ParseUint(getLine(), 10, 32)

		for lines > 0 {
			line := getLine()

			if _, ok := accounts[line]; ok {
				accounts[line]++
			} else {
				accounts[line] = 1
			}
			lines--
		}

		solve(accounts)

		tasks--
		if tasks > 0 {
			Print("\n")
			getLine() // read & skip "\n"
		}
	}
}

func getLine() string {
	line, _ := bio.ReadString(0x0A)
	return strings.TrimSpace(line)
}

func solve(accounts map[string]uint32) []string {
	numbers := make([]string, 0, len(accounts))
	for n := range accounts {
		numbers = append(numbers, n)
	}
	sort.Strings(numbers)

	for _, n := range numbers {
		Printf(n+" %d\n", accounts[n])
	}

	return numbers
}
