defmodule Day01Test do
  use ExUnit.Case, async: true
  import Advent.Day01

  @moduletag :day01

  @example1 """
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
  """

  setup_all do
    {:ok, data} = File.read("/data/day01.txt")
    {:ok, data: data}
  end

  describe "examples" do
    @tag examples: :part1
    test "part1" do
      assert part1(@example1) == 24000
    end

    @tag examples: :part2
    test "part2" do
      assert part2(@example1) == 45000
    end
  end

  describe "solutions" do
    @tag solutions: :part1
    test "part1", state do
      assert part1(state[:data]) == 68775
    end

    @tag solutions: :part2
    test "part2", state do
      assert part2(state[:data]) == 202585
    end
  end
end
