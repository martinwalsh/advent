from day07 import part1, part2

EXAMPLE1 = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_examples():
    assert part1(EXAMPLE1) == 95437
    assert part2(EXAMPLE1) == 24933642


def test_solution_part1(load_input):
    with load_input("/data/day07.txt") as data:
        assert part1(data) == 1989474


def test_solution_part2(load_input):
    with load_input("/data/day07.txt") as data:
        assert part2(data) == 1111607
