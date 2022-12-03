#!/usr/bin/env python
import string

SCORES = {k: v for k, v in zip(string.ascii_letters, range(1, 53))}


def parse(data):
    for line in data.splitlines():
        yield line[: len(line) // 2], line[len(line) // 2 :]


def take3(generator):
    try:
        while True:
            yield [next(generator) for _ in range(3)]
    except StopIteration:
        return


def part1(data):
    scores = []
    for c1, c2 in parse(data):
        for letter in c1:
            if letter in c2:
                scores.append(SCORES[letter])
                break
    return sum(scores)


def part2(data):
    scores = []
    for (a1, a2), (b1, b2), (c1, c2) in take3(parse(data)):
        for letter in a1 + a2:
            if letter in (b1 + b2) and letter in (c1 + c2):
                scores.append(SCORES[letter])
                break
    return sum(scores)
