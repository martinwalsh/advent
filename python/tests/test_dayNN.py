from dayNN import part1, part2


def test_examples():
    assert True, 'Add tests for the example data described in the puzzle'


def test_solution_part1(load_input):
    with load_input('/data/dayNN-YYYY.txt') as data:
        assert part1(data) is NotImplemented


def test_solution_part2(load_input):
    with load_input('/data/dayNN-YYYY.txt') as data:
        assert part2(data) is NotImplemented
