import pytest

from day11 import part1, part2, power


def test_example_power_levels():
    assert power(3, 5, 8) == 4
    assert power(122, 79, 57) == -5
    assert power(217, 196, 39) == 0
    assert power(101, 153, 71) == 4


def test_example_part1():
    assert part1(18) == (33, 45)
    assert part1(42) == (21, 61)


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_example_part2():
    assert part2(18) == (90, 269, 16)
    assert part2(42) == (232, 251, 12)


def test_solution_part1():
    assert part1(7347) == (243, 17)


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_part2():
    assert part2(7347) == (233, 228, 12)
