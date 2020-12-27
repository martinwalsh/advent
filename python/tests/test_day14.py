from day14 import part1, part2


EXAMPLE1 = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


EXAMPLE2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


def test_examples():
    assert part1(EXAMPLE1) == 165
    assert part2(EXAMPLE2) == 208


def test_solution_part1(load_input):
    with load_input('/data/day14-2020.txt') as data:
        assert part1(data) == 10717676595607


def test_solution_part2(load_input):
    with load_input('/data/day14-2020.txt') as data:
        assert part2(data) == 3974538275659
