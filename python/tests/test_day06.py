from day06 import part1, part2

EXAMPLE1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
EXAMPLE2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
EXAMPLE3 = "nppdvjthqldpwncqszvftbrmjlhg"
EXAMPLE4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
EXAMPLE5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def test_examples():
    assert part1(EXAMPLE1) == 7
    assert part1(EXAMPLE2) == 5
    assert part1(EXAMPLE3) == 6
    assert part1(EXAMPLE4) == 10
    assert part1(EXAMPLE5) == 11

    assert part2(EXAMPLE1) == 19
    assert part2(EXAMPLE2) == 23
    assert part2(EXAMPLE3) == 23
    assert part2(EXAMPLE4) == 29
    assert part2(EXAMPLE5) == 26


def test_solution_part1(load_input):
    with load_input("/data/day06.txt") as data:
        assert part1(data) == 1965


def test_solution_part2(load_input):
    with load_input("/data/day06.txt") as data:
        assert part2(data) == 2773
