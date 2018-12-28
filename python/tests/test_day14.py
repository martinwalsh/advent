import pytest

from day14 import part1, part2


def test_examples_part1():
    assert part1(9) == '5158916779'
    assert part1(5) == '0124515891'
    assert part1(18) == '9251071085'
    assert part1(2018) == '5941429882'


def test_solution_part1():
    assert part1(846601) == '3811491411'


def test_examples_part2():
    assert part2(51589) == 9
    assert part2('01245') == 5
    assert part2(92510) == 18
    assert part2(59414) == 2018


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_part2():
    assert part2(846601) == 20408083
