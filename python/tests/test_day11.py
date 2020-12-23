import pytest

from day11 import part1, part2

EXAMPLE1 = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


def test_examples():
    assert part1(EXAMPLE1) == 37
    assert part2(EXAMPLE1) == 26


@pytest.mark.slow
def test_solution_part1(load_input):
    with load_input('/data/day11-2020.txt') as data:
        assert part1(data) == 2178


@pytest.mark.slow
def test_solution_part2(load_input):
    with load_input('/data/day11-2020.txt') as data:
        assert part2(data) is NotImplemented
