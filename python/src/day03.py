#!/usr/bin/env python
import re
from itertools import product
from collections import defaultdict

# updated with improvements from
# https://github.com/petertseng/adventofcode-rb-2018/blob/master/03_grid_claims.rb


class Fabric(object):
    def __init__(self):
        self.squares = defaultdict(list)
        self.all_ids = set()

    def place(self, claim):
        _id, left, top, width, height = claim
        for x, y in product(range(left, left + width),
                            range(top, top + height)):
            self.squares[(x, y)].append(_id)
            self.all_ids.add(_id)

    @property
    def overlap(self):
        return [ids for (x, y), ids in self.squares.items() if len(ids) > 1]

    @classmethod
    def from_records(cls, records):
        claims = []
        pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

        for record in records:
            try:
                _id, left, top, width, height = \
                        map(int, pattern.search(record).groups())
            except (AttributeError, ValueError):
                raise ValueError(f'Invalid claim record format: {record}')
            claims.append((_id, left, top, width, height))

        fabric = cls()
        for claim in claims:
            fabric.place(claim)

        return fabric


def part1(records):
    fabric = Fabric.from_records(records)
    return len(fabric.overlap)


def part2(records):
    fabric = Fabric.from_records(records)
    overlap_ids = set()
    for ids in fabric.overlap:
        overlap_ids.update(ids)
    return fabric.all_ids.difference(overlap_ids).pop()
