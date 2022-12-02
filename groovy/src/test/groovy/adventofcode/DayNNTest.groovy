package adventofcode

import spock.lang.Specification

class DayNNTestCls extends Specification {
  def dayNN = new DayNN()
  String data = new File('/data/dayNN.txt').text

  String EXAMPLE = """\
  """

  def "check examples"() {
    expect:
      dayNN.part1(EXAMPLE) != false
      dayNN.part2(EXAMPLE) != false
  }

  def "check part 1"() {
    expect: dayNN.part1() != false
  }

  def "check part 2"() {
    expect: dayNN.part2() != false
  }
}