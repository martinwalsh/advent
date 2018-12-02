package adventofcode

import spock.lang.Specification

class DayNNTest extends Specification {
  def dayNN = new DayNN()

  def "check part 1"() {
    expect: dayNN.part1() != false
  }

  def "check part 2"() {
    expect: dayNN.part2() != false
  }

  def "can read data file"() {
    setup:
    String data = new File('/data/dayNN.txt').text

    expect: data == ''
  }
}
