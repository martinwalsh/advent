import pytest
from day05 import part1, part2

EXAMPLES_PART1 = [
    ('aA', ''),
    ('abBA', ''),
    ('abAB', 'abAB'),
    ('aabAAB', 'aabAAB'),
    ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
]


@pytest.mark.parametrize('polymer,expected', EXAMPLES_PART1)
def test_examples_part1(polymer, expected):
    assert part1(polymer) == expected


def test_examples_part2():
    assert part2('dabAcCaCBAcCcaDA') == 4


def test_solution_part1(load_input):
    with load_input('/data/day05-mw.txt') as data:
        assert len(part1(data.strip())) == 10878


def test_solution_part2(load_input):
    with load_input('/data/day05-mw.txt') as data:
        assert part2(data.strip()) == 6874
