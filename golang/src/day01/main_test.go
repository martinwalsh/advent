package day01

import (
	"bufio"
	"github.com/franela/goblin"
	. "github.com/onsi/gomega"
	"log"
	"os"
	"testing"
)

func load_data(path string) []string {
	var lines []string
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return lines
}

func TestDay01Part1(t *testing.T) {
	g := goblin.Goblin(t)

	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check part 1 examples", func() {
		g.It("should correctly adjust frequencies", func() {
			example1 := []string{"+1", "+1", "+1"}
			example2 := []string{"+1", "+1", "-2"}
			example3 := []string{"-1", "-2", "-3"}

			Expect(part1(example1)).To(Equal(3))
			Expect(part1(example2)).To(Equal(0))
			Expect(part1(example3)).To(Equal(-6))
		})
	})

	g.Describe("real input for part 1", func() {
		g.It("should correctly adjust frequencies", func() {
			Expect(part1(load_data("/data/day01-2018.txt"))).To(Equal(582))
		})
	})
}

func TestDay01Part2(t *testing.T) {
	g := goblin.Goblin(t)

	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check part 2 examples", func() {
		g.It("should correctly calibrate", func() {
			Expect(part2([]string{"+1", "-1"})).To(Equal(0))
			Expect(part2([]string{"+3", "+3", "+4", "-2", "-4"})).To(Equal(10))
			Expect(part2([]string{"-6", "+3", "+8", "+5", "-6"})).To(Equal(5))
			Expect(part2([]string{"+7", "+7", "-2", "-7", "-4"})).To(Equal(14))
		})
	})

	g.Describe("real input for part 2", func() {
		g.It("should correctly calibrate", func() {
			Expect(part2(load_data("/data/day01-2018.txt"))).To(Equal(488))
		})
	})
}
