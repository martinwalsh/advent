defmodule Advent.Day02 do
  use Advent.Input.IntegerData, delimiter: ","

  @opcodes %{
    1 => &Kernel.+/2,
    2 => &Kernel.*/2
  }

  defp reset(p1 \\ 12, p2 \\ 2) do
    data()
    |> List.replace_at(1, p1)
    |> List.replace_at(2, p2)
  end

  def part1() do
    reset()
    |> compute()
    |> List.first()
  end

  def part2() do
    {noun, verb} =
      for(p1 <- 0..99, p2 <- 0..99, do: {p1, p2})
      |> Enum.find(fn {p1, p2} ->
        reset(p1, p2) |> compute() |> List.first() == 19_690_720
      end)

    100 * noun + verb
  end

  def compute(program, pointer \\ 0) do
    [opcode, p1, p2, p3] = fetch_all(program, pointer..(pointer + 3))

    case opcode do
      99 ->
        program

      op ->
        value =
          @opcodes
          |> Map.fetch!(op)
          |> Kernel.apply(fetch_all(program, [p1, p2]))

        compute(List.replace_at(program, p3, value), pointer + 4)
    end
  end

  defp fetch_all(seq, indices, default \\ nil) do
    Enum.map(indices, fn i -> Enum.at(seq, i, default) end)
  end
end
