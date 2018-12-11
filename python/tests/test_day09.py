import pytest
from day09 import solve


EXAMPLES = [
    (9, 32, 25),
    (10, 8317, 1618),
    (13, 146373, 7999),
    (17, 2764, 1104),
    (21, 54718, 6111),
    (30, 37305, 5807),
]


@pytest.mark.parametrize('num_players,score,num_marbles', EXAMPLES)
def test_examples_part1(num_players, num_marbles, score):
    assert solve(num_players, num_marbles) == score


def test_solution_part1():
    assert solve(470, 72170) == 388024


@pytest.mark.skipif(pytest.config.getoption('--run-slow'),
                    reason='use --run-slow to run slow tests')
def test_solution_part2(load_input):
    assert solve(470, 72170 * 100) == 3180929875
