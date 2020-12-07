#!/usr/bin/env python
from functools import reduce
from itertools import permutations


def part1(text, k=2):
    for items in permutations(map(int, text.strip().splitlines()), k):
        if sum(items) == 2020:
            return reduce(int.__mul__, items)
    else:
        raise RuntimeError('Invalid input: no pair with sum 2020 found.')


def part2(text):
    return part1(text, k=3)
