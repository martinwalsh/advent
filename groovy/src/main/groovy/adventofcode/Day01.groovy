package adventofcode

class Day01 {
  def parse(String data) {
    def elves = data.trim().split('\n\n')
    elves.collect { elf ->
      elf.tokenize("\n").collect { cal -> cal.toInteger() }.sum()
    }
  }

  Integer part1(String data) {
    parse(data).max()
  }

  Integer part2(String data) {
    def sums = parse(data)
    sums.sort { -it }
    return sums[0..2].sum()
  }
}
