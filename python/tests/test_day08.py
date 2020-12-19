from day08 import part1, part2

EXAMPLE1 = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_examples():
    assert part1(EXAMPLE1) == 5
    assert part2(EXAMPLE1) == 8


def test_solution_part1(load_input):
    with load_input('/data/day08-2020.txt') as data:
        assert part1(data) == 2058


def test_solution_part2(load_input):
    with load_input('/data/day08-2020.txt') as data:
        assert part2(data) == 1000
