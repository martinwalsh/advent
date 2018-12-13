import pytest

from day10 import part1, Point

EXAMPLE_INPUT = """\
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
""".splitlines()

EXAMPLE_POINTS = [
    ((9,  1), (0,  2)),
    ((7,  0), (-1,  0)),
    ((3, -2), (-1,  1)),
    ((6, 10), (-2, -1)),
    ((2, -4), (2,  2)),
    ((-6, 10), (2, -2)),
    ((1,  8), (1, -1)),
    ((1,  7), (1,  0)),
    ((-3, 11), (1, -2)),
    ((7,  6), (-1, -1)),
    ((-2,  3), (1,  0)),
    ((-4,  3), (2,  0)),
    ((10, -3), (-1,  1)),
    ((5, 11), (1, -2)),
    ((4,  7), (0, -1)),
    ((8, -2), (0,  1)),
    ((15,  0), (-2,  0)),
    ((1,  6), (1,  0)),
    ((8,  9), (0, -1)),
    ((3,  3), (-1,  1)),
    ((0,  5), (0, -1)),
    ((-2,  2), (2,  0)),
    ((5, -2), (1,  2)),
    ((1,  4), (2,  1)),
    ((-2,  7), (2, -2)),
    ((3,  6), (-1, -1)),
    ((5,  0), (1,  0)),
    ((-6,  0), (2,  0)),
    ((5,  9), (1, -2)),
    ((14,  7), (-2,  0)),
    ((-3,  6), (2, -1)),
]


EXAMPLE_EXPECTED = """\
#...#..###
#...#...#.
#...#...#.
#####...#.
#...#...#.
#...#...#.
#...#...#.
#...#..###
"""


@pytest.mark.parametrize('record,expected',
                         zip(EXAMPLE_INPUT, EXAMPLE_POINTS))
def test_example_parse(record, expected):
    point = Point.from_record(record)
    assert (point.position, point.velocity) == expected


def test_example_parts_1_and_2():
    assert part1(EXAMPLE_INPUT) == (3, EXAMPLE_EXPECTED)


SOLUTION_EXPECTED = """\
######.....###..######..######....##......##....#####...######
#...........#........#..#........#..#....#..#...#....#..#.....
#...........#........#..#.......#....#..#....#..#....#..#.....
#...........#.......#...#.......#....#..#....#..#....#..#.....
#####.......#......#....#####...#....#..#....#..#####...#####.
#...........#.....#.....#.......######..######..#.......#.....
#...........#....#......#.......#....#..#....#..#.......#.....
#.......#...#...#.......#.......#....#..#....#..#.......#.....
#.......#...#...#.......#.......#....#..#....#..#.......#.....
######...###....######..######..#....#..#....#..#.......######
"""


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_parts_1_and_2(load_input):
    with load_input('/data/day10-2018.txt') as data:
        assert part1(data.splitlines()) == (10054, SOLUTION_EXPECTED)
