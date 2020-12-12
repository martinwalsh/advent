#!/usr/bin/env python

from functools import reduce


class Grid:
    def __init__(self, text):
        self.data = [list(line) for line in text.splitlines()]

        self.max_y = len(self.data) - 1
        self.max_x = len(self.data[0]) - 1

    def is_tree(self, x, y):
        return self.data[y][x] == '#'


class Toboggan:
    def __init__(self, grid, slope, start=(0, 0)):
        self.grid = grid

        self.pos_x, self.pos_y = start
        self.slope_x, self.slope_y = slope

    @property
    def position(self):
        return (self.pos_x, self.pos_y)

    def __iter__(self):
        while self.pos_y < self.grid.max_y:
            self.pos_x = (self.pos_x + self.slope_x) % (self.grid.max_x + 1)
            self.pos_y = self.pos_y + self.slope_y
            yield self.position

    @classmethod
    def trees(cls, grid, slope):
        return len([(x, y) for x, y in cls(grid, slope) if grid.is_tree(x, y)])


def part1(text):
    grid = Grid(text)
    return Toboggan.trees(grid, (3, 1))


def part2(text):
    grid = Grid(text)
    return reduce(int.__mul__, (Toboggan.trees(grid, p) for p in ((1, 1),
                                                                  (3, 1),
                                                                  (5, 1),
                                                                  (7, 1),
                                                                  (1, 2),)))
