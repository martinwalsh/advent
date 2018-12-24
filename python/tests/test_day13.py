from day13 import part1, part2, Map, D


EXAMPLE1 = r"""
/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
""".lstrip()


EXAMPLE2 = r"""
/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
""".lstrip()


def test_example_parse_map():
    tracks = ''.join(EXAMPLE1.replace(' ', '').splitlines())
    tmap = Map(EXAMPLE1)

    assert len(tmap.tracks) == len(tracks)
    assert len(tmap.carts) == 2


def test_input_data_parse_map(load_input):
    with load_input('/data/day13-2018.txt') as data:
        tracks = ''.join(data.replace(' ', '').splitlines())
        tmap = Map(data)
        assert len(tmap.tracks) == len(tracks)
        assert len(tmap.carts) == 17


def test_direction_motion():
    assert (0, 0) >> D.N == (0, -1)
    assert (0, 0) >> D.S == (0, 1)
    assert (0, 0) >> D.E == (1, 0)
    assert (0, 0) >> D.W == (-1, 0)


def test_turn_direction_cycle():
    assert D.N ^ '<' == D.W
    assert D.N ^ '>' == D.E
    assert D.E ^ '<' == D.N
    assert D.W ^ '<' == D.S
    assert D.N ^ '^' == D.N


def test_turn_direction_inverse_of_enter_direction():
    assert ~D.N == D.S
    assert ~D.S == D.N
    assert ~D.E == D.W
    assert ~D.W == D.E


def test_turn_direction_track_exits():
    assert D.N | '|' == D.N   # enter heading north (from the south), exit to the north
    assert D.E | '-' == D.E   # enter heading east (from the west), exit to the east
    assert D.E | '/' == D.N   # enter heading east (from the west), exit to the north
    assert D.S | '\\' == D.E  # enter heading south (from the north), exit to the east


def test_example_part1():
    assert part1(EXAMPLE1) == (7, 3)


def test_example_part2():
    assert part2(EXAMPLE2) == (6, 4)


def test_solution_part1(load_input):
    with load_input('/data/day13-2018.txt') as data:
        assert part1(data) == (117, 62)


def test_solution_part2(load_input):
    with load_input('/data/day13-2018.txt') as data:
        assert part2(data) == (69, 67)
