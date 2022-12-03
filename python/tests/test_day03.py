from day03 import part1, part2


EXAMPLE1 = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_examples():
    assert part1(EXAMPLE1) == 157
    assert part2(EXAMPLE1) == 70


def test_solution_part1(load_input):
    with load_input("/data/day03.txt") as data:
        assert part1(data) == 7817


def test_solution_part2(load_input):
    with load_input("/data/day03.txt") as data:
        assert part2(data) == 2444
