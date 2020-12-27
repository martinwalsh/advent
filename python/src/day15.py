#!/usr/bin/env python
# from functools import partial
# from collections import deque, defaultdict


def parse(text):
    return [int(n) for n in text.strip().split(',')]


def insert(d, k, value):
    if k in d:
        d[k] = (value, d[k][0])
    else:
        d[k] = (value,)


def play(seed):
    d = {}
    # d = defaultdict(partial(deque, [], 2))
    turn = 1
    for number in seed:
        yield number
        insert(d, number, turn)
        # d[number].appendleft(turn)
        turn += 1

    while True:
        try:
            number = int.__sub__(*d[number])
        except TypeError:
            number = 0

        yield number
        insert(d, number, turn)
        # d[number].appendleft(turn)
        turn += 1


def takeN(g, n=2020):
    for _ in range(n):
        result = next(g)
    return result


def part1(text):
    return takeN(play(parse(text)))


def part2(text):
    return takeN(play(parse(text)), 30000000)
