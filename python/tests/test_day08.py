from day08 import part1, part2

EXAMPLE1 = """\
30373
25512
65332
33549
35390
"""


def test_examples():
    assert part1(EXAMPLE1) == 21
    assert part2(EXAMPLE1) == 8


def test_solution_part1(load_input):
    with load_input("/data/day08.txt") as data:
        assert part1(data) == 1715


def test_solution_part2(load_input):
    with load_input("/data/day08.txt") as data:
        assert part2(data) == 374400
