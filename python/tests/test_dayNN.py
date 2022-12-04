from dayNN import part1, part2

EXAMPLE1 = """\
"""


def test_examples():
    assert part1(EXAMPLE1) is NotImplemented
    assert part2(EXAMPLE1) is NotImplemented


def test_solution_part1(load_input):
    with load_input("/data/dayNN.txt") as data:
        assert part1(data) is NotImplemented


def test_solution_part2(load_input):
    with load_input("/data/dayNN.txt") as data:
        assert part2(data) is NotImplemented
