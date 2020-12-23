#!/usr/bin/env python


class Grid:
    _directions = {
        'nw': lambda x, y, o: (x - o, y - o),
        'n': lambda x, y, o: (x, y - o),
        'ne': lambda x, y, o: (x + o, y - o),
        'e': lambda x, y, o: (x + o, y),
        'se': lambda x, y, o: (x + o, y + o),
        's': lambda x, y, o: (x, y + o),
        'sw': lambda x, y, o: (x - o, y + o),
        'w': lambda x, y, o: (x - o, y),
    }

    def __init__(self, grid, stand_when_occupied=4, to_next_visible=False):
        self.grid = grid
        self.to_next_visible = to_next_visible
        self.stand_when_occupied = stand_when_occupied
        self.max_offset = max(y for x, y in self.grid)

    def _get_adjacent(self, x, y):
        for move in self._directions.values():
            if self.to_next_visible:
                for offset in range(1, self.max_offset + 1):
                    node = move(x, y, offset)
                    if node in self.grid:
                        if self.grid[node] == '.':
                            continue
                        yield node
                    break
            else:
                node = move(x, y, 1)
                if node in self.grid:
                    yield node

    def _get_adjacent_values(self, x, y):
        return [self.grid[xx, yy] for xx, yy in self._get_adjacent(x, y)]

    def step(self):
        grid = self.grid.copy()
        for x, y in self.grid:
            # Fill the seat
            if self.grid[x, y] == 'L' and \
                    '#' not in self._get_adjacent_values(x, y):
                grid[x, y] = '#'
            # Vacate the seat
            if self.grid[x, y] == '#' and \
                    self._get_adjacent_values(x, y).count('#') >= self.stand_when_occupied:
                grid[x, y] = 'L'
        self.grid = grid
        return self.to_string()

    def to_string(self):
        rows = []
        for y in range(max(y for x, y in self.grid) + 1):
            row = []
            for x in range(max(x for x, y in self.grid) + 1):
                row.append(self.grid[x, y])
            rows.append(row)
        return '\n'.join(''.join(row) for row in rows)

    def count(self, value):
        return self.to_string().count(value)

    @classmethod
    def parse(cls, text, stand=4, visible=False):
        grid = {}
        for y, row in enumerate(text.splitlines()):
            for x, value in enumerate(row):
                grid[(x, y)] = value
        return cls(grid, stand, visible)


def part1(text, stand=4, visible=False):
    grid = Grid.parse(text, stand, visible)
    lastval = ''
    while True:
        updated = grid.step()
        if lastval == updated:
            break
        lastval = updated
    return grid.count('#')


def part2(text):
    return part1(text, 5, True)
