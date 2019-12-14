defmodule Day02Test do
  use ExUnit.Case, async: true
  import Advent.Day02

  test "examples_part1" do
    assert compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) |> List.first() == 3500
    assert compute([1, 0, 0, 0, 99]) |> List.first() == 2
    assert compute([2, 3, 0, 3, 99]) |> Enum.at(3) == 6
    assert compute([2, 4, 4, 5, 99, 0]) |> Enum.at(-1) == 9801
    assert compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) |> List.first() == 30
    assert compute([1, 1, 1, 4, 99, 5, 6, 0, 99]) |> Enum.at(4) == 2
  end

  test "part1" do
    assert part1() == 4_576_384
  end

  @tag :skip
  test "part2" do
    assert part2() == 5_398
  end
end
