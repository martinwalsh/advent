#!/usr/bin/env python


def parse(data, length=4):
    for i in range(len(data) - length + 1):
        yield i, data[i : i + length]


def part1(data):
    for i, segment in parse(data, 4):
        if len(set(segment)) == 4:
            return i + 4


def part2(data):
    for i, segment in parse(data, 14):
        if len(set(segment)) == 14:
            return i + 14
