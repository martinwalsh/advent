#!/usr/bin/env python
from collections import Counter
from itertools import combinations


def check(identifier):
    return set(v for v in Counter(identifier).values() if 2 <= v <= 3)


def part1(ids):
    counter = Counter()
    for identifier in ids:
        counter.update(check(identifier))
    return counter[2] * counter[3]


def part2(ids):
    for a, b in combinations(ids, 2):
        common = ''.join(x for x, y in zip(a, b) if x == y)
        if len(common) == len(a) - 1:
            return common
    raise ValueError('Invalid input: no fabric boxes found')
