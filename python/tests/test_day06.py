from day06 import part1, part2

EXAMPLE1 = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_examples():
    assert part1(EXAMPLE1) == 11
    assert part2(EXAMPLE1) == 6


def test_solution_part1(load_input):
    with load_input('/data/day06-2020.txt') as data:
        assert part1(data) == 6885


def test_solution_part2(load_input):
    with load_input('/data/day06-2020.txt') as data:
        assert part2(data) == 3550
