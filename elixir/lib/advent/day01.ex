defmodule Advent.Day01 do
  use Advent.Input.IntegerData, delimiter: "\n"

  def part1() do
    Enum.map(data(), &calculate_fuel/1) |> sum()
  end

  def part2() do
    Enum.map(data(), &calculate_fuel_with_fuel_cost/1) |> sum()
  end

  def calculate_fuel(mass) do
    Kernel.trunc(mass / 3) - 2
  end

  def calculate_fuel_with_fuel_cost(mass) do
    case calculate_fuel(mass) do
      n when n <= 0 ->
        0

      n ->
        n + calculate_fuel_with_fuel_cost(n)
    end
  end
end
