defmodule Advent.Day01 do
  @spec parse(String.t) :: integer
  def parse(data) do
    data = String.trim(data)
    groups = String.split(data, "\n\n")
    Enum.map(groups, fn (g) ->
      calories = String.split(g, "\n")
      Enum.sum(Enum.map(calories, fn (s) ->
        String.to_integer(s)
      end))
    end)
  end

  @spec part1(String.t) :: integer
  def part1(data) do
    Enum.max(parse(data))
  end

  @spec part2(String.t) :: integer
  def part2(data) do
    Enum.sum(Enum.take(Enum.sort(parse(data), :desc), 3))
  end
end
