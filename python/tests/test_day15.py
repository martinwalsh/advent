import pytest

from day15 import part1, part2


EXAMPLE_PART1_1 = """\
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""

EXAMPLE_PART1_2 = """\
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""

EXAMPLE_PART1_3 = """\
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""

EXAMPLE_PART1_4 = """\
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""

EXAMPLE_PART1_5 = """\
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""

EXAMPLE_PART1_6 = """\
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
"""

EXAMPLES_PART1 = {
    (EXAMPLE_PART1_1, 47, 27730),
    (EXAMPLE_PART1_2, 37, 36334),
    (EXAMPLE_PART1_3, 46, 39514),
    (EXAMPLE_PART1_4, 35, 27755),
    (EXAMPLE_PART1_5, 54, 28944),
    (EXAMPLE_PART1_6, 20, 18740),
}


@pytest.mark.parametrize('data,rounds,score', EXAMPLES_PART1)
def test_examples_part1(data, rounds, score):
    battle = part1(data)
    assert battle.rounds == rounds
    assert battle.score == score


def test_solution_part1(load_input):
    with load_input('/data/day15-2018.txt') as data:
        battle = part1(data)
        assert battle.score == 207059


EXAMPLES_PART2 = {
    (EXAMPLE_PART1_1, 29, 4988, 15),
    (EXAMPLE_PART1_3, 33, 31284, 4),
    (EXAMPLE_PART1_4, 37, 3478, 15),
    (EXAMPLE_PART1_5, 39, 6474, 12),
    (EXAMPLE_PART1_6, 30, 1140, 34),
}


@pytest.mark.parametrize('data,rounds,score,elf_power', EXAMPLES_PART2)
def test_examples_part2(data, rounds, score, elf_power):
    battle, power = part2(data)
    assert battle.rounds == rounds
    assert battle.score == score
    assert power == elf_power


def test_solution_part2(load_input):
    with load_input('/data/day15-2018.txt') as data:
        battle, power = part2(data)
        assert battle.score == 49120
