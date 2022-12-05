from day05 import part1, part2

EXAMPLE1 = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """


def test_examples():
    assert part1(EXAMPLE1) == "CMZ"
    assert part2(EXAMPLE1) == "MCD"


def test_solution_part1(load_input):
    with load_input("/data/day05.txt") as data:
        assert part1(data) == "FRDSQRRCD"


def test_solution_part2(load_input):
    with load_input("/data/day05.txt") as data:
        assert part2(data) == "HRFTQVWNN"
