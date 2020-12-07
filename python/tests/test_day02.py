from day02 import part1, part2

EXAMPLE_PART1 = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def test_examples():
    assert part1(EXAMPLE_PART1) == 2
    assert part2(EXAMPLE_PART1) == 1


def test_solution_part1(load_input):
    with load_input(f'/data/day02-2020.txt') as data:
        assert part1(data) == 458


def test_solution_part2(load_input):
    with load_input(f'/data/day02-2020.txt') as data:
        assert part2(data) == 342
