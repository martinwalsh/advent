import pytest
from day03 import part1, part2, Fabric

EXAMPLE1 = [
    ("#1 @ 1,3: 4x4", (1, 1, 3, 4, 4)),
    ("#2 @ 3,1: 4x4", (2, 3, 1, 4, 4)),
    ("#3 @ 5,5: 2x2", (3, 5, 5, 2, 2)),
]


@pytest.mark.parametrize('record,expected', EXAMPLE1)
def test_examples_record_parser(record, expected):
    fabric, claims = Fabric.from_records([record])
    assert claims[0] == expected


def test_examples_overlap():
    assert part1([X[0] for X in EXAMPLE1]) == 4


def test_solution_part1(load_input):
    with load_input('/data/day03-marty.txt') as data:
        assert part1(data.splitlines()) == 105231


def test_solution_part2(load_input):
    with load_input('/data/day03-marty.txt') as data:
        assert part2(data.splitlines()) == 164
