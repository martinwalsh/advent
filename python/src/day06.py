#!/usr/bin/env python
from typing import NamedTuple
from collections import Counter
from itertools import product, starmap


class Point(NamedTuple):
    x: int = float('inf')
    y: int = float('inf')

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __bool__(self):
        return (self.x, self.y) != (float('inf'), float('inf'))


class Grid(object):
    def __init__(self, records):
        self.points = sorted(starmap(Point, (map(int, record.split(', ')) for record in records)))
        xmin, xmax, ymin, ymax = (
            min(p.x for p in self.points),
            max(p.x for p in self.points),
            min(p.y for p in self.points),
            max(p.y for p in self.points),
        )
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.origins = starmap(Point, product(range(xmin, xmax+1), range(ymin, ymax+1)))

    def largest_finite_area(self):
        infinite = set()
        area = Counter()

        for origin in self.origins:
            nearest, nearest_distance = Point(), float('inf')
            for point in self.points:
                distance = point.distance(origin)
                if distance == nearest_distance:
                    nearest = Point()  # min distance is the same for more than one point
                elif distance < nearest_distance:
                    nearest_distance, nearest = distance, point

            if nearest:
                if origin.x in (self.xmin, self.xmax) \
                        or origin.y in (self.ymin, self.ymax):
                    infinite.add(nearest)
                area[nearest] += 1

        for point, size in area.most_common():
            if point not in infinite:
                return size
        else:
            raise ValueError('Invalid input: no non-infinite area found')

    def count_safe_origins(self, limit=32):
        safe = 0
        for origin in self.origins:
            if sum(point.distance(origin) for point in self.points) < limit:
                safe += 1
        return safe


def part1(records):
    return Grid(records).largest_finite_area()


def part2(records, limit=32):
    return Grid(records).count_safe_origins(limit)
