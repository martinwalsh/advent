from day07 import part1, part2, extract


EXAMPLE = """\
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".splitlines()


def test_example_extract():
    assert list(extract(EXAMPLE)) == [
        ('C', 'A'), ('C', 'F'), ('A', 'B'),
        ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E'),
    ]


def test_example_part1():
    assert part1(EXAMPLE) == 'CABDFE'


def test_example_part2():
    assert part2(EXAMPLE) == 15


def test_solution_part1(load_input):
    with load_input('/data/day07-2018.txt') as data:
        assert part1(data.splitlines()) == 'ACBDESULXKYZIMNTFGWJVPOHRQ'


def test_solution_part2(load_input):
    with load_input('/data/day07-2018.txt') as data:
        assert part2(data.splitlines(), workers=5, step_duration=60) == 980
