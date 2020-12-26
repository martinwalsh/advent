#!/usr/bin/env python
from itertools import count
from functools import reduce


def parse(text, include_skipped=False):
    start, ids = text.rstrip().splitlines()
    ids = [
        (minute, int(_id)) for minute, _id in enumerate(ids.split(',')) if _id.isnumeric()
    ]
    return int(start), ids


def scheduled(start, ids):
    for tick in count(start):
        for _, _id in ids:
            if tick % _id == 0:
                yield tick, _id
                break


# def timestamps_by_multiples_of_first(ids):
#     first = ids[0][1]
#     while True:
#         yield [first] + [first + m for m, _ in ids[1:]]
#         first += ids[0][1]
#
#
# def timestamps_by_multiples_of_largest(ids):
#     offset, step = max(ids, key=lambda x: x[1])
#     counter = step
#     while True:
#         first = counter - offset
#         yield [first] + [first + m for m, _ in ids[1:]]
#         counter += step
#
#
# def multiples(ids, sequence=timestamps_by_multiples_of_first):
#     for timestamps in sequence(ids):
#         for idx, _id in enumerate(timestamps):
#             if ids[idx][1] % _id != 0:
#                 break
#         else:
#             return timestamps[0]


# Needed hint, found solution.
# See https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
def by_prime_products(ids):
    # FIXME: Can we start at the max id here, as in timestamps_by_multiples_of_largest?
    size = 2
    timestamp = inc = ids[0][1]
    while True:
        busses = ids[:size]
        while not all((s + timestamp) % b == 0 for s, b in busses):
            timestamp += inc

        inc = reduce(int.__mul__, (b for _, b in busses), 1)
        size += 1

        if len(busses) == len(ids):
            break
    return timestamp


def part1(text):
    start, ids = parse(text)
    schedule = scheduled(start, ids)
    tick, _id = next(schedule)
    return (tick - start) * _id


def part2(text):
    _, ids = parse(text)
    return by_prime_products(ids)
