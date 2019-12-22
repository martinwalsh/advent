defmodule Day04Test do
  use ExUnit.Case, async: true
  import Advent.Day04

  test "examples_part1" do
    assert is_valid_password?("111111") == true
    assert is_valid_password?("223450") == false
    assert is_valid_password?("123789") == false

    assert is_valid_password?("999999", :part1, 100_000, 199_999) == false
  end

  test "examples_part2" do
    assert is_valid_password?("112233", :part2) == true
    assert is_valid_password?("123444", :part2) == false
    assert is_valid_password?("111122", :part2) == true
  end

  @tag :skip
  test "part1" do
    assert part1() == 1929
  end

  @tag :skip
  test "part2" do
    assert part2() == 1306
  end
end
