package main

import (
    "testing"
    "github.com/franela/goblin"
    . "github.com/onsi/gomega"
)

func TestDayNNPart1(t *testing.T) {
    g := goblin.Goblin(t)

    RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

    g.Describe("check part 1", func() {
      g.It("is true", func() {
        Expect(dayNN_part1()).To(BeTrue())
      })
    })
}

func TestDayNNPart2(t *testing.T) {
    g := goblin.Goblin(t)

    RegisterFailHandler(func(m string, _ ...int) { g.Fail(m) })

    g.Describe("check part 2", func() {
      g.It("is true", func() {
        Expect(dayNN_part2()).To(BeTrue())
      })
    })
}
