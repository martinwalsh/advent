package adventofcode

import spock.lang.Specification


class Day01TestCls extends Specification {
  String EXAMPLE1 = """\
  1000
  2000
  3000

  4000

  5000
  6000

  7000
  8000
  9000

  10000"""

  def day01 = new Day01()
  String data = new File('/data/day01.txt').text

  def "check examples"() {
    expect:
    day01.part1(EXAMPLE1) == 24000
    day01.part2(EXAMPLE1) == 45000
  }

  def "check part 1"() {
    expect: day01.part1(data) == 68775
  }

  def "check part 2"() {
    expect: day01.part2(data) == 202585
  }
}
