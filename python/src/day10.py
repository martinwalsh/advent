#!/usr/bin/env python
import re


class Point(object):
    _pattern = re.compile(
        r'position=<((?:\s*-?\d+),(?:\s*-?\d+))> velocity=<((?:\s*-?\d+),(?:\s*-?\d+))>'
    )

    def __init__(self, position, velocity):
        self.x, self.y = self.position = position
        self.velocity = velocity

    def __iter__(self):
        pos = self.position
        while True:
            yield pos
            pos = tuple(a + b for a, b in zip(pos, self.velocity))

    @classmethod
    def from_record(cls, record):
        position, velocity = cls._pattern.search(record).groups()
        return cls(
            tuple(int(pair) for pair in position.split(', ')),
            tuple(int(pair) for pair in velocity.split(', ')),
        )


class Snapshot(object):
    def __init__(self, points):
        self.xmin, self.xmax, self.ymin, self.ymax = (
            min(x for x, y in points),
            max(x for x, y in points),
            min(y for x, y in points),
            max(y for x, y in points),
        )
        self.points = points

    def to_str(self):
        rows = ''
        for y in range(self.ymin, self.ymax + 1):
            row = ''
            for x in range(self.xmin, self.xmax + 1):
                row += '#' if (x, y) in self.points else '.'
            rows += f'{row}\n'
        return rows

    @property
    def has_message(self):
        x_values = {x for (x, y) in self.points}
        for x in x_values:
            y_values = {y for (_x, y) in self.points if _x == x}
            if len(y_values) >= self.ymax - self.ymin:
                return True


class Grid(object):
    def __init__(self, points):
        self.points = [iter(p) for p in points]

    def __iter__(self):
        time = 0
        while True:
            yield time, Snapshot({next(p) for p in self.points})
            time += 1

    @classmethod
    def from_records(cls, records):
        return cls([Point.from_record(record) for record in records])


def part1(records):
    for time, snapshot in iter(Grid.from_records(records)):
        if snapshot.has_message:
            return time, snapshot.to_str()
