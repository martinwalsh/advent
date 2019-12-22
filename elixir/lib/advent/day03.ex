defmodule Advent.Day03 do
  alias Advent.Input.DirectionalData

  use DirectionalData
  @behaviour DirectionalData

  def part1() do
    data()
    |> closest_intersection()
    |> manhattan_distance()
  end

  def closest_intersection([wire1, wire2]) do
    MapSet.intersection(wire1, wire2)
    |> Enum.to_list()
    |> Enum.min_by(fn {x, y} -> manhattan_distance({x, y}) end)
  end

  def manhattan_distance({x, y}) do
    Kernel.abs(0 - x) + Kernel.abs(0 - y)
  end

  @impl DirectionalData
  def collect(csv) do
    {coords, _} =
      String.split(csv, ",")
      |> Enum.flat_map_reduce({0, 0}, fn vector, {x, y} ->
        points = collect({x, y}, vector)
        {points, points |> List.last()}
      end)

    coords
  end

  def collect(origin, <<direction::binary-size(1), distance::binary>>) do
    collect(origin, direction, String.to_integer(distance))
  end

  def collect({origin_x, origin_y} = origin, direction, distance) do
    Stream.unfold(origin, fn {x, y} ->
      case direction do
        "R" ->
          if x == origin_x + distance, do: nil, else: {{x + 1, y}, {x + 1, y}}

        "L" ->
          if x == origin_x - distance, do: nil, else: {{x - 1, y}, {x - 1, y}}

        "U" ->
          if y == origin_y + distance, do: nil, else: {{x, y + 1}, {x, y + 1}}

        "D" ->
          if y == origin_y - distance, do: nil, else: {{x, y - 1}, {x, y - 1}}
      end
    end)
    |> Enum.to_list()
  end
end
