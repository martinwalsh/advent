#!/usr/bin/env python
from itertools import permutations


def parse(text):
    return [int(line) for line in text.splitlines()]


def moving(numbers, start=0, size=5):
    while start+size < len(numbers):
        yield numbers[start+size], numbers[start:start+size]
        start += 1


def is_valid(number, items):
    for a, b in permutations(set(items), 2):
        if a + b == number:
            return True
    else:
        return False


def part1(text, size=5):
    for n, window in moving(parse(text), size=size):
        if not is_valid(n, window):
            return n


def part2(text, size=5):
    broken = part1(text, size)
    numbers = parse(text)
    idx = numbers.index(broken)
    matchset = numbers[:idx]
    for length in range(idx, 1, -1):
        for start in range(0, len(matchset) - length):
            if sum(matchset[start:start+length]) == broken:
                return min(matchset[start:start+length]) + max(matchset[start:start+length])
