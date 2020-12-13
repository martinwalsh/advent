from day05 import part1, part2

EXAMPLE1 = """\
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""


def test_examples():
    assert part1(EXAMPLE1) == [357, 567, 119, 820]


def test_solution_part1(load_input):
    with load_input('/data/day05-2020.txt') as data:
        assert max(part1(data)) == 926


def test_solution_part2(load_input):
    with load_input('/data/day05-2020.txt') as data:
        assert part2(data) == 657
