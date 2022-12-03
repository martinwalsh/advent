from day02 import part1, part2


EXAMPLE1 = """\
A Y
B X
C Z
""".strip()


def test_examples():
    assert part1(EXAMPLE1) == 15
    assert part2(EXAMPLE1) == 12


def test_solution_part1(load_input):
    with load_input("/data/day02.txt") as data:
        assert part1(data) == 11063


def test_solution_part2(load_input):
    with load_input("/data/day02.txt") as data:
        assert part2(data) == 10349
