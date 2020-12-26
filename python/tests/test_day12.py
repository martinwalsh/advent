from day12 import part1, part2

EXAMPLE1 = """\
F10
N3
F7
R90
F11
"""


def test_examples():
    assert part1(EXAMPLE1) == 25
    assert part2(EXAMPLE1) == 286


def test_solution_part1(load_input):
    with load_input('/data/day12-2020.txt') as data:
        assert part1(data) == 1186


def test_solution_part2(load_input):
    with load_input('/data/day12-2020.txt') as data:
        assert part2(data) == 47806
