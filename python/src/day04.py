#!/usr/bin/env python


def parse(data):
    for line in data.splitlines():
        yield [[int(s) for s in e.split("-")] for e in line.split(",")]


def part1(data):
    return len(
        [
            e1a
            for (e1a, e1b), (e2a, e2b) in parse(data)
            if (e1a >= e2a and e1b <= e2b) or (e2a >= e1a and e2b <= e1b)
        ]
    )


def part2(data):
    return len(
        [
            e1a
            for (e1a, e1b), (e2a, e2b) in parse(data)
            if (e2a <= e1a <= e2b or e2a <= e1b <= e2b)
            or (e1a <= e2a <= e1b or e1a <= e2b <= e1b)
        ]
    )
