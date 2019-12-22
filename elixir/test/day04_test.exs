defmodule Day04Test do
  use ExUnit.Case, async: true
  import Advent.Day04

  test "examples_part1" do
    assert is_valid_password?("111111") == true
    assert is_valid_password?("223450") == false
    assert is_valid_password?("123789") == false

    assert is_valid_password?("999999", 10000..19999) == false
  end

  test "part1" do
    assert part1() == 1929
  end
end
