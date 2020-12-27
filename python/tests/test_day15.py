import pytest

from day15 import part1, part2

EXAMPLE1 = """\
0,3,6
"""

EXAMPLE2 = """\
1,3,2
"""

EXAMPLE3 = """\
2,1,3
"""

EXAMPLE4 = """\
1,2,3
"""

EXAMPLE5 = """\
2,3,1
"""

EXAMPLE6 = """\
3,2,1
"""

EXAMPLE7 = """\
3,1,2
"""


def test_examples_part1():
    assert part1(EXAMPLE1) == 436
    assert part1(EXAMPLE2) == 1
    assert part1(EXAMPLE3) == 10
    assert part1(EXAMPLE4) == 27
    assert part1(EXAMPLE5) == 78
    assert part1(EXAMPLE6) == 438
    assert part1(EXAMPLE7) == 1836


@pytest.mark.slow
def test_exampes_part2():
    assert part2(EXAMPLE1) == 175594
    assert part2(EXAMPLE2) == 2578
    assert part2(EXAMPLE3) == 3544142
    assert part2(EXAMPLE4) == 261214
    assert part2(EXAMPLE5) == 6895259
    assert part2(EXAMPLE6) == 18
    assert part2(EXAMPLE7) == 362


def test_solution_part1(load_input):
    with load_input('/data/day15-2020.txt') as data:
        assert part1(data) == 1085


@pytest.mark.slow
def test_solution_part2(load_input):
    with load_input('/data/day15-2020.txt') as data:
        assert part2(data) == 10652
