defmodule Day03Test do
  use ExUnit.Case, async: true
  import Advent.Day03

  test "examples_part1" do
    [wire1, wire2] = ["R8,U5,L5,D3", "U7,R6,D4,L4"] |> Enum.map(&collect/1)

    assert length(wire1) == 8 + 5 + 5 + 3
    assert length(wire2) == 7 + 6 + 4 + 4

    closest =
      [wire1, wire2]
      |> closest_by(:manhattan)

    assert closest == {3, 3}
    assert manhattan_distance(closest) == 6

    assert [
             "R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83"
           ]
           |> Enum.map(&collect/1)
           |> closest_by(:manhattan)
           |> manhattan_distance() == 159

    assert [
             "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
             "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
           ]
           |> Enum.map(&collect/1)
           |> closest_by(:manhattan)
           |> manhattan_distance() == 135
  end

  test "part1" do
    assert part1() == 403
  end

  test "examples_part2" do
    [wire1, wire2] =
      ["R8,U5,L5,D3", "U7,R6,D4,L4"]
      |> Enum.map(&collect/1)

    assert [wire1, wire2] |> closest_by(:sum_of_steps) == {6, 5}
    assert sum_of_steps({6, 5}, wire1, wire2) == 30

    [wire1, wire2] =
      [
        "R75,D30,R83,U83,L12,D49,R71,U7,L72",
        "U62,R66,U55,R34,D71,R55,D58,R83"
      ]
      |> Enum.map(&collect/1)

    closest = closest_by([wire1, wire2], :sum_of_steps)
    assert sum_of_steps(closest, wire1, wire2) == 610

    [wire1, wire2] =
      [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
      ]
      |> Enum.map(&collect/1)

    closest = closest_by([wire1, wire2], :sum_of_steps)
    assert sum_of_steps(closest, wire1, wire2) == 410
  end

  test "part2" do
    assert part2() == 4158
  end
end
