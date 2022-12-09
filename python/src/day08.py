#!/usr/bin/env python
from functools import reduce
from collections import defaultdict


def parse(data):
    trees = {}
    for y, row in enumerate(data.splitlines()):
        for x, column in enumerate(row):
            trees[(x, y)] = int(column)
    return trees


def part1(data):
    trees = parse(data)
    max_x, max_y = [n + 1 for n in max(trees)]

    visible = max_y * 2 + max_x * 2 - 4

    for y in range(1, max_y - 1):
        for x in range(1, max_x - 1):
            # up
            for _y in range(y - 1, -1, -1):
                if trees[(x, _y)] >= trees[(x, y)]:
                    break
            else:
                visible += 1
                continue

            # down
            for _y in range(y + 1, max_y):
                if trees[(x, _y)] >= trees[(x, y)]:
                    break
            else:
                visible += 1
                continue

            # left
            for _x in range(x - 1, -1, -1):
                if trees[(_x, y)] >= trees[(x, y)]:
                    break
            else:
                visible += 1
                continue

            # right
            for _x in range(x + 1, max_x):
                if trees[(_x, y)] >= trees[(x, y)]:
                    break
            else:
                visible += 1

    return visible


def part2(data):
    trees = parse(data)
    visibility = defaultdict(int)
    directions = defaultdict(int)
    max_x, max_y = [n + 1 for n in max(trees)]

    for y in range(1, max_y - 1):
        for x in range(1, max_x - 1):
            # up
            for _y in range(y - 1, -1, -1):
                directions[(x, y, 0)] += 1
                if trees[(x, _y)] >= trees[(x, y)]:
                    break

            # down
            for _y in range(y + 1, max_y):
                directions[(x, y, 1)] += 1
                if trees[(x, _y)] >= trees[(x, y)]:
                    break

            # left
            for _x in range(x - 1, -1, -1):
                directions[(x, y, 2)] += 1
                if trees[(_x, y)] >= trees[(x, y)]:
                    break

            # right
            for _x in range(x + 1, max_x):
                directions[(x, y, 3)] += 1
                if trees[(_x, y)] >= trees[(x, y)]:
                    break

            visibility[(x, y)] = reduce(
                int.__mul__, (directions[(x, y, i)] for i in range(4))
            )

    return max(visibility.values())
