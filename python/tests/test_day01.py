from day01 import part1, part2


def test_examples_part1():
    example1 = "+1 +1 +1".split()
    example2 = "+1 +1 -2".split()
    example3 = "-1 -2 -3".split()

    assert part1(example1) == 3
    assert part1(example2) == 0
    assert part1(example3) == -6


def test_examples_part2():
    example1 = "+1 -1".split()
    example2 = "+3 +3 +4 -2 -4".split()
    example3 = "-6 +3 +8 +5 -6".split()
    example4 = "+7 +7 -2 -7 -4".split()

    assert part2(example1) == 0
    assert part2(example2) == 10
    assert part2(example3) == 5
    assert part2(example4) == 14


def test_solution_part1(load_input):
    with load_input('/data/day01-marty.txt') as data:
        assert part1(data.splitlines()) == 582


def test_solution_part2(load_input):
    with load_input('/data/day01-marty.txt') as data:
        assert part2(data.splitlines()) == 488
