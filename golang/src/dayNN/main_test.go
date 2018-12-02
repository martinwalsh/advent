package dayNN

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

func TestDayNNPart1(t *testing.T) {
	g := goblin.Goblin(t)

	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check part 1", func() {
		g.It("is true", func() {
			Expect(part1()).To(BeTrue())
		})

		g.It("can read a data file", func() {
			var expected []string
			Expect(load_data("/data/dayNN.txt")).To(Equal(expected))
		})
	})
}

func TestDayNNPart2(t *testing.T) {
	g := goblin.Goblin(t)

	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check part 2", func() {
		g.It("is true", func() {
			Expect(part2()).To(BeTrue())
		})
	})
}
