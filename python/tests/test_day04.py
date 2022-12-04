from day04 import part1, part2


EXAMPLE1 = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_examples():
    assert part1(EXAMPLE1) == 2
    assert part2(EXAMPLE1) == 4


def test_solution_part1(load_input):
    with load_input("/data/day04.txt") as data:
        assert part1(data) == 459


def test_solution_part2(load_input):
    with load_input("/data/day04.txt") as data:
        assert part2(data) == 779
