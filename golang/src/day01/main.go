package day01

import (
	"log"
	"strconv"
)

// https://softwareengineering.stackexchange.com/questions/177428/sets-data-structure-in-golang
type IntSet struct {
	set map[int]bool
}

func NewIntSet() *IntSet {
	return &IntSet{make(map[int]bool)}
}

func (set *IntSet) Add(i int) bool {
	_, found := set.set[i]
	set.set[i] = true
	return !found
}

func (set *IntSet) Contains(i int) bool {
	_, found := set.set[i]
	return found
}

//

func calibrate(seq []string, freq int) chan int {
	c := make(chan int)

	go func() {
		for _, value := range seq {
			v, err := strconv.Atoi(value)
			if err != nil {
				log.Fatal(err)
			}
			freq += v
			c <- freq
		}
		close(c)
	}()

	return c
}

func part1(seq []string) int {
	// FIXME: hrm, there must be a better way to grab the last element
	var result int
	for freq := range calibrate(seq, 0) {
		result = freq
	}
	return result
}

func part2(seq []string) int {
	seen := NewIntSet()
	seen.Add(0)

	retries := 1
	current := 0

	for retries < 1000 {
		for freq := range calibrate(seq, current) {
			if seen.Contains(freq) {
				return freq
			}
			seen.Add(freq)
			current = freq
		}
		retries += 1
	}

	log.Fatal("Invalid input: reached retry limit")

	return 0
}
