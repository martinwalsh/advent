defmodule Day01 do
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

  defp sum(numbers) do
    Enum.reduce(numbers, 0, fn n, acc -> n + acc end)
  end

  defp data do
    File.read!("/data/day01-2019.txt")
    |> String.split("\n")
    |> Enum.drop(-1)
    |> Enum.map(&String.to_integer/1)
  end
end
