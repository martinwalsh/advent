from day01 import part1, part2

EXAMPLE_PART1 = """\
1721
979
366
299
675
1456
"""

def test_examples():
    assert part1(EXAMPLE_PART1) == 514579
    assert part2(EXAMPLE_PART1) == 241861950


def test_solution_part1(load_input):
    with load_input(f'/data/day01-2020.txt') as data:
        assert part1(data) == 290784


def test_solution_part2(load_input):
    with load_input(f'/data/day01-2020.txt') as data:
        assert part2(data) == 177337980
