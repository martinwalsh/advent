defmodule Advent.Day04 do
  use Advent.Input.RangeData

  @digits Enum.map(0..9, &Integer.to_string/1)

  def part1 do
    {first, last, data} = data()

    data
    |> Enum.filter(fn password -> is_valid_password?(password, :part1, first, last) end)
    |> length()
  end

  def part2 do
    {first, last, data} = data()

    data
    |> Enum.filter(fn password ->
      is_valid_password?(password, :part2, first, last)
    end)
    |> length()
  end

  def is_valid_password?(password, part \\ :part1, first \\ 0, last \\ 999_999) do
    password_as_int = String.to_integer(password)

    cond do
      String.length(password) != 6 ->
        false

      password_as_int < first or password_as_int > last ->
        false

      password != sorted(password) ->
        false

      !Enum.any?(@digits, fn digit ->
        case part do
          :part1 ->
            String.contains?(password, String.duplicate(digit, 2))

          :part2 ->
            String.contains?(password, String.duplicate(digit, 2)) and
                not String.contains?(password, String.duplicate(digit, 3))
        end
      end) ->
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
