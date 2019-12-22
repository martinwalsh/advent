defmodule Advent.Day04 do
  use Advent.Input.RangeData

  @adjacents Enum.map(0..9, fn n -> "#{n}#{n}" end)

  def part1 do
    {first, last, data} = data()

    data
    |> Enum.filter(fn password ->
      is_valid_password?(password, first..last)
    end)
    |> length()
  end

  def is_valid_password?(password, range \\ 0..999_999) do
    cond do
      String.length(password) != 6 ->
        false

      String.to_integer(password) not in range ->
        false

      password != sorted(password) ->
        false

      !Enum.any?(@adjacents, fn nn -> String.contains?(password, nn) end) ->
        false

      true ->
        true
    end
  end

  defp sorted(string) do
    String.split(string, "", trum: true)
    |> Enum.sort()
    |> Enum.join("")
  end
end
