from day01 import part1, part2


EXAMPLE1 = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_examples():
    assert part1(EXAMPLE1) == 24000
    assert part2(EXAMPLE1) == 45000


def test_solution_part1(load_input):
    with load_input("/data/day01.txt") as data:
        assert part1(data) == 68775


def test_solution_part2(load_input):
    with load_input("/data/day01.txt") as data:
        assert part2(data) == 202585
