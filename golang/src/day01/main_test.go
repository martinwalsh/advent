package day01

import (
	"bufio"
	"log"
	"os"
	"strings"
	"testing"

	"github.com/franela/goblin"
	. "github.com/onsi/gomega"
)

var EXAMPLE1 string = `
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
`

func TestDay01Examples(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check examples", func() {
		g.It("is correct", func() {
			Expect(part1(EXAMPLE1)).To(Equal(int64(24000)))
			Expect(part2(EXAMPLE1)).To(Equal(int64(45000)))
		})
	})
}

func TestDay01Part1(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	data := load_data("/data/day01.txt")

	g.Describe("check part 1", func() {
		g.It("is correct", func() {
			Expect(part1(data)).To(Equal(int64(68775)))
		})
	})
}

func TestDay01Part2(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	data := load_data("/data/day01.txt")

	g.Describe("check part 2", func() {
		g.It("is correct", func() {
			Expect(part2(data)).To(Equal(int64(202585)))
		})
	})
}

func load_data(path string) string {
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

	return strings.Join(lines, "\n")
}
