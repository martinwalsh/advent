from day03 import part1, part2

EXAMPLE1 = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

def test_examples():
    assert part1(EXAMPLE1) == 7
    assert part2(EXAMPLE1) == 336


def test_solution_part1(load_input):
    with load_input(f'/data/day03-2020.txt') as data:
        assert part1(data) == 156


def test_solution_part2(load_input):
    with load_input(f'/data/day03-2020.txt') as data:
        assert part2(data)  == 3521829480
