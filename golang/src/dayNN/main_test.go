package dayNN

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
`

func TestDayNNExamples(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	g.Describe("check examples", func() {
		g.It("is correct", func() {
			Expect(part1(EXAMPLE1)).To(BeTrue())
			Expect(part2(EXAMPLE1)).To(BeTrue())
		})
	})
}

func TestDayNNPart1(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	data := load_data("/data/dayNN.txt")

	g.Describe("check part 1", func() {
		g.It("is correct", func() {
			Expect(part1(data)).To(BeTrue())
		})
	})
}

func TestDayNNPart2(t *testing.T) {
	g := goblin.Goblin(t)
	RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

	data := load_data("/data/dayNN.txt")

	g.Describe("check part 2", func() {
		g.It("is correct", func() {
			Expect(part2(data)).To(BeTrue())
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
