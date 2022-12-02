#!/usr/bin/env python
from collections import Counter

def parse(data):
    return [sum(int(item) for item in elf.splitlines()) for elf in data.split("\n\n")]

def part1(data):
    return max(parse(data))


def part2(data):
    return sum(sorted(parse(data), reverse=True)[:3])
