from day08 import part1, part2, Node

EXAMPLE = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'


def test_example_parse_tree_metadata():
    assert sum(Node.from_records(EXAMPLE.split()).metadata) == 138


def test_example_parse_tree_value():
    assert Node.from_records(EXAMPLE.split()).value == 66


def test_solution_part1(load_input):
    with load_input('/data/day08-2018.txt') as data:
        assert part1(data) == 46578


def test_solution_part2(load_input):
    with load_input('/data/day08-2018.txt') as data:
        assert part2(data) == 31251
