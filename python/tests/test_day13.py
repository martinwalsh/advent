import pytest

from day13 import part1, part2


EXAMPLE1 = """\
939
7,13,x,x,59,x,31,19
"""

EXAMPLE2 = """\
0
17,x,13,19
"""

EXAMPLE3 = """\
0
67,7,59,61
"""

EXAMPLE4 = """\
0
67,x,7,59,61
"""

EXAMPLE5 = """\
0
67,7,x,59,61
"""

EXAMPLE6 = """\
0
1789,37,47,1889
"""


def test_part1_examples():
    assert part1(EXAMPLE1) == 295


def test_part2_examples():
    assert part2(EXAMPLE1) == 1068781
    assert part2(EXAMPLE2) == 3417
    assert part2(EXAMPLE3) == 754018
    assert part2(EXAMPLE4) == 779210
    assert part2(EXAMPLE5) == 1261476
    assert part2(EXAMPLE6) == 1202161486


def test_solution_part1(load_input):
    with load_input('/data/day13-2020.txt') as data:
        assert part1(data) == 161


def test_solution_part2(load_input):
    with load_input('/data/day13-2020.txt') as data:
        assert part2(data) == 213890632230818
