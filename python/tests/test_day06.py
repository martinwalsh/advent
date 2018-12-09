import pytest
from day06 import part1, part2, Grid, Point

EXAMPLE = """\
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""


def test_example_parse_records():
    assert Grid(EXAMPLE.splitlines()).points == [
        Point(x, y) for x, y in [(1, 1), (1, 6), (3, 4), (5, 5), (8, 3), (8, 9)]
    ]


def test_example_point_distance():
    assert Point(1, 4).distance(Point(1, 6)) == 2
    assert Point(1, 4).distance(Point(3, 4)) == 2
    assert Point(0, 4).distance(Point(1, 6)) == 3
    assert Point(0, 4).distance(Point(3, 4)) == 3

    assert Point(1, 6).distance(Point(1, 4)) == 2
    assert Point(3, 4).distance(Point(0, 4)) == 3


def test_example_part1():
    assert part1(EXAMPLE.splitlines()) == 17


def test_example_safe_locations():
    assert part2(EXAMPLE.splitlines()) == 16


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_part1(load_input):
    with load_input('/data/day06-2018.txt') as data:
        assert part1(data.splitlines()) == 3882


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_part2(load_input):
    with load_input('/data/day06-2018.txt') as data:
        assert part2(data.splitlines(), 10000) == 43852
