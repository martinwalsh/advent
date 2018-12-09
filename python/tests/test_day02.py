import pytest
from day02 import part1, part2, check

PART1_EXAMPLES = [
    ('abcdef', set()),
    ('bababc', {2, 3}),
    ('abbcde', {2}),
    ('abcccd', {3}),
    ('aabcdd', {2}),
    ('abcdee', {2}),
    ('ababab', {3}),
]


PART2_EXAMPLES = """\
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""


@pytest.mark.parametrize('_input,expected', PART1_EXAMPLES)
def test_examples_check_function(_input, expected):
    assert check(_input) == expected


def test_examples_checksum_function():
    assert part1(_id for _id, ans in PART1_EXAMPLES) == 12


def test_solution_part1(load_input):
    with load_input('/data/day02-2018.txt') as data:
        assert part1(data.splitlines()) == 8296


def test_examples_common_characters():
    assert part2(PART2_EXAMPLES.splitlines()) == 'fgij'


def test_solution_part2(load_input):
    with load_input('/data/day02-2018.txt') as data:
        assert part2(data.splitlines()) == 'pazvmqbftrbeosiecxlghkwud'
