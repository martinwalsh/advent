package day01

import (
	"sort"
	"strconv"
	"strings"
)

func parse(data string) []int64 {
	var calories []int64
	for _, elf := range strings.Split(data, "\n\n") {
		var total int64 = 0
		for _, s := range strings.Split(elf, "\n") {
			i, _ := strconv.ParseInt(s, 10, 64)
			total += i
		}
		calories = append(calories, total)
	}
	return calories
}

func reversed(calories []int64) []int64 {
	sort.SliceStable(calories, func(i, j int) bool {
		return calories[i] > calories[j]
	})
	return calories
}

func part1(data string) int64 {
	return reversed(parse(data))[0]
}

func part2(data string) int64 {
	var total int64
	for _, i := range reversed(parse(data))[0:3] {
		total += i
	}
	return total
}
