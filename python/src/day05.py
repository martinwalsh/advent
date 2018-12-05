#!/usr/bin/env python
from string import ascii_lowercase as lc


def match(a, b):
    return a != b and a.lower() == b.lower()


def annihilate(polymer):
    stack = []
    for char in polymer:
        if stack and match(stack[-1], char):
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def part1(polymer):
    return annihilate(polymer)


def part2(polymer):
    def purge(letter, source):
        return source.replace(letter, '').replace(letter.upper(), '')
    return min(len(annihilate(purge(x, polymer))) for x in lc)
