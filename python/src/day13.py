#!/usr/bin/env python
from enum import Enum
from itertools import cycle


class D(Enum):
    N = (0, -1)
    S = (0, 1)
    E = (1, 0)
    W = (-1, 0)

    @classmethod
    def by_value(cls, value):
        return {'^': cls.N, 'v': cls.S, '<': cls.W, '>': cls.E}[value]

    @classmethod
    def by_direction(cls, direction):
        return {cls.N: '^', cls.S: 'v', cls.W: '<', cls.E: '>'}[direction]

    def __rrshift__(self, other):        # (0, 0) >> D.N == (0, -1)
        ax, ay = other
        bx, by = self.value
        return (ax + bx, ay + by)

    def __xor__(self, other):            # D.N ^ '<' == D.W
        return {
            D.N: {'<': D.W, '>': D.E},
            D.S: {'<': D.E, '>': D.W},
            D.E: {'<': D.N, '>': D.S},
            D.W: {'<': D.S, '>': D.N},
        }[self].get(other, self)

    def __or__(self, other):             # D.N | '|' == D.S
        return {
            '-': {D.E: D.W, D.W: D.E},
            '|': {D.N: D.S, D.S: D.N},
            '/': {D.N: D.W, D.W: D.N, D.S: D.E, D.E: D.S},
            '\\': {D.N: D.E, D.E: D.N, D.S: D.W, D.W: D.S},
        }[other][~self]

    def __invert__(self):                # ~D.N == D.S
        return {D.N: D.S, D.S: D.N, D.E: D.W, D.W: D.E}[self]


class Cart(object):
    def __init__(self, value, position):
        self.position = position
        self.direction = D.by_value(value)
        self.turns = cycle(('<', '^', '>'))

    def turn(self, track):
        if track == '+':
            self.direction ^= next(self.turns)
        else:
            self.direction |= track

    def move(self):
        self.position >>= self.direction

    def __repr__(self):
        return '<Cart: {} `{}`>'.format(self.position, D.by_direction(self.direction))


class Map(object):
    def __init__(self, data):
        self.tracks = {}
        self.carts = set()
        for y, line in enumerate(data.splitlines()):
            for x, value in enumerate(line):
                if value in '<>^v':
                    self.carts.add(Cart(value, (x, y)))
                    value = dict(zip('<>^v', '--||'))[value]
                if value != ' ':
                    self.tracks[(x, y)] = value

    def tick(self, return_on_collision=True):
        for cart in sorted(self.carts, key=lambda c: c.position[::-1]):
            cart.move()
            if self.crashed(cart):
                if not return_on_collision:
                    self.carts = set(c for c in self.carts if c.position != cart.position)
                    continue
                else:
                    return cart.position
            cart.turn(self.tracks[cart.position])

    def crashed(self, cart):
        return any(c.position == cart.position for c in self.carts if c is not cart)

    def __repr__(self):
        rows = []
        carts = {cart.position: cart for cart in self.carts}
        for y in range(0, max(y for x, y in self.tracks) + 1):
            row = []
            for x in range(0, max(x for x, y in self.tracks) + 1):
                if (x, y) in self.tracks:
                    if (x, y) in carts:
                        m = '\033[1;32m{}\033[0;0m'.format(D.by_direction(carts[(x, y)].direction))
                        row.append(m)
                    else:
                        row.append(self.tracks[(x, y)])
                else:
                    row.append(' ')
            rows.append(''.join(row))
        return '\n'.join(rows)


def debug(map):
    print(f'{map}')
    print(f'{map.carts}')
    input()


def part1(data, _debug=False):
    map = Map(data)
    if _debug: debug(map)      # noqa: E701
    while True:
        coords = map.tick()
        if coords:
            return coords
        if _debug: debug(map)  # noqa: E701


def part2(data, _debug=False):
    map = Map(data)
    if _debug: debug(map)      # noqa: E701
    while len(map.carts) > 1:
        map.tick(False)
        if _debug: debug(map)  # noqa: E701
    return map.carts.pop().position


EXAMPLE1 = r"""
/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/
""".lstrip()

EXAMPLE2 = r"""
/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/
""".lstrip()


if __name__ == '__main__':
    print(part1(EXAMPLE1, True))
    print(part2(EXAMPLE2, True))

    # with open('/data/day13-2018.txt') as f:
    #     print(part1(f.read(), True))

    # with open('/data/day13-2018.txt') as f:
    #     print(part2(f.read(), True))
