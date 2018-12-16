#!/usr/bin/env python


def power(x, y, serial):
    return int(str(((x + 10) * y + serial) * (x + 10))[-3]) - 5


class SummedAreaTable(object):
    def __init__(self, serial, size=3):
        self.size = size
        cumsum = {}
        for y in range(1, 301):
            for x in range(1, 301):
                cumsum[(x, y)] = (
                    power(x, y, serial)
                    + cumsum.get((x, y - 1), 0)
                    + cumsum.get((x - 1, y), 0)
                    - cumsum.get((x - 1, y - 1), 0)
                )
        self.cumsum = cumsum

    def _sum(self, x, y):
        return (
            self.cumsum[(x + self.size, y + self.size)]
            + self.cumsum[(x, y)]
            - self.cumsum[(x + self.size, y)]
            - self.cumsum[(x, y + self.size)]
        )

    def largest(self):
        if self.size == 300:
            return self.cumsum[(300, 300)], (1, 1)

        return max((
            (self._sum(x, y), (x+1, y+1))
            for x, y in self.cumsum
            if x < (301 - self.size) and y < (301 - self.size)
        ))


def part1(serial):
    return SummedAreaTable(serial).largest()[1]


def part2(serial):
    total, (x, y), size = max((SummedAreaTable(serial, n).largest() + (n,) for n in range(1, 301)))
    return (x, y, size)
