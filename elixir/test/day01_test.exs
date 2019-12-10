defmodule Day01Test do
  use ExUnit.Case
  import Day01

  test "example_part1" do
    assert calculate_fuel(12) == 2
  end

  test "part1" do
    assert part1() == 3_317_659
  end
end
