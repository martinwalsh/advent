defmodule DayNNTest do
  use ExUnit.Case, async: true
  import Advent.DayNN

  @moduletag :dayNN
  @example1 """
  """

  setup_all do
    {:ok, data} = File.read("/data/dayNN.txt")
    {:ok, data: data}
  end

  describe "examples" do
    @tag examples: :part1
    test "part1" do
      assert part1(@example1) == nil
    end

    @tag examples: :part2
    test "part2" do
      assert part2(@example1) == nil
    end
  end

  describe "solutions" do
    @tag solutions: :part1
    test "part1", state do
      assert part1(state[:data]) == nil
    end

    @tag solutions: :part2
    test "part2", state do
      assert part2(state[:data]) == nil
    end
  end
end
