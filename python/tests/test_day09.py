from day09 import part1, part2

EXAMPLE1 = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


def test_examples():
    assert part1(EXAMPLE1) == 127
    assert part2(EXAMPLE1) == 62


def test_solution_part1(load_input):
    with load_input('/data/day09-2020.txt') as data:
        assert part1(data, 25) == 776203571


def test_solution_part2(load_input):
    with load_input('/data/day09-2020.txt') as data:
        assert part2(data, 25) == 104800569
