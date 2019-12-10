defmodule Day01 do
  def part1() do
    data()
    |> Enum.reduce(0, fn n, acc -> acc + calculate_fuel(n) end)
  end

  def calculate_fuel(mass) do
    Kernel.trunc(mass / 3) - 2
  end

  defp data do
    File.read!("/data/day01-2019.txt")
    |> String.split(~r/\R/)
    |> Enum.filter(&(&1 != ""))
    |> Enum.map(fn line ->
      {n, ""} = Integer.parse(line)
      n
    end)
  end
end
