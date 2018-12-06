from day03 import part1, part2

EXAMPLE = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2",
]


def test_examples_overlap():
    assert part1(EXAMPLE) == 4


def test_examples_no_overlap():
    assert part2(EXAMPLE) == 3


def test_solution_part1(load_input):
    with load_input('/data/day03-marty.txt') as data:
        assert part1(data.splitlines()) == 105231


def test_solution_part2(load_input):
    with load_input('/data/day03-marty.txt') as data:
        assert part2(data.splitlines()) == 164
