defmodule Day01Test do
  use ExUnit.Case, async: true
  import Advent.Day01

  test "examples_part1" do
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100_756) == 33583
  end

  test "example_part2" do
    assert calculate_fuel_with_fuel_cost(14) == 2
    assert calculate_fuel_with_fuel_cost(1969) == 966
    assert calculate_fuel_with_fuel_cost(100_756) == 50346
  end

  test "part1" do
    assert part1() == 3_317_659
  end

  test "part2" do
    assert part2() == 4_973_616
  end
end
