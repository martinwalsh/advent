from day10 import part1, part2

EXAMPLE1 = """\
16
10
15
5
1
11
7
19
6
12
4
"""

EXAMPLE2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


def test_examples():
    assert part1(EXAMPLE2) == 220
    assert part2(EXAMPLE1) == 8
    assert part2(EXAMPLE2) == 19208


def test_solution_part1(load_input):
    with load_input('/data/day10-2020.txt') as data:
        assert part1(data) == 1820


def test_solution_part2(load_input):
    with load_input('/data/day10-2020.txt') as data:
        assert part2(data) == 3454189699072
