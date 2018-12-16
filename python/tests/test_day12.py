from day12 import part1, part2, parse_input


EXAMPLE = """\
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".splitlines()


def test_example_parse_input():
    initial, rules = parse_input(EXAMPLE)
    assert initial == '#..#.#..##......###...###'
    assert rules['...##'] == '#'
    assert rules['####.'] == '#'


def test_example_part1():
    assert part1(EXAMPLE) == 325


def test_solution_part1(load_input):
    with load_input('/data/day12-2018.txt') as data:
        assert part1(data.splitlines()) == 2444


def test_solution_part2(load_input):
    with load_input('/data/day12-2018.txt') as data:
        assert part2(data.splitlines()) == 750000000697
