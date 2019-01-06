from day16 import part1, part2, parse


EXAMPLE_PART1 = """\
Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]


"""


def test_parse_example_part1():
    samples, program = parse(EXAMPLE_PART1)

    assert program == []
    assert len(samples) == 1

    sample = samples[0]
    assert sample.after == [3, 2, 2, 1]
    assert sample.before == [3, 2, 1, 1]
    assert sample.operation == [9, 2, 1, 2]


def test_parse_part1_data(load_input):
    with load_input('/data/day16-2018.txt') as data:
        samples, program = parse(data)
        assert len(samples) == 782
        assert len(program) == 892


def test_example_part1():
    assert part1(EXAMPLE_PART1) == 1


def test_solution_part1(load_input):
    with load_input('/data/day16-2018.txt') as data:
        assert part1(data) == 590


def test_solution_part2(load_input):
    with load_input('/data/day16-2018.txt') as data:
        assert part2(data) == 475
