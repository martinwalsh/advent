#!/usr/bin/env python
import re
from itertools import product
from collections import namedtuple


class Fabric(object):
    pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    claim = namedtuple('Claim', ['id', 'left', 'top', 'width', 'height'])

    def __init__(self, maxx, maxy):
        self.squares = {}
        self.maxx = maxx
        self.maxy = maxy
        for x, y in product(range(maxx), range(maxy)):
            self.squares[(x, y)] = -1

    def place(self, claim, attempt=0):
        it_overlaps = False
        for x, y in product(range(claim.left, claim.left + claim.width),
                            range(claim.top, claim.top + claim.height)):
            self.squares[(x, y)] = self.squares[(x, y)] + 1
            if self.squares[(x, y)] > attempt:
                it_overlaps = True
        return it_overlaps

    def get_overlap(self):
        for x, y in product(range(self.maxx), range(self.maxy)):
            if self.squares[(x, y)] > 0:
                yield (x, y)

    @classmethod
    def from_records(cls, records):
        claims = []
        for record in records:
            try:
                _id, left, top, width, height = \
                        map(int, cls.pattern.search(record).groups())
            except (AttributeError, ValueError):
                raise ValueError(f'Invalid claim record format: {record}')
            claims.append(cls.claim(_id, left, top, width, height))

        maxx = max(c.left + c.width for c in claims)
        maxy = max(c.top + c.height for c in claims)
        return cls(maxx, maxy), claims


def part1(records):
    fabric, claims = Fabric.from_records(records)
    for claim in claims:
        fabric.place(claim)
    return len(list(fabric.get_overlap()))


def part2(records):
    fabric, claims = Fabric.from_records(records)
    no_overlaps = [claim for claim in claims if not fabric.place(claim)]
    while no_overlaps:
        claim = no_overlaps.pop()
        if not fabric.place(claim, 1):
            return claim.id
