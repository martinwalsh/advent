#!/usr/bin/env python


class Seat:
    def __init__(self, text):
        self._rows = text[0:7]
        self._columns = text[7:10]

    @staticmethod
    def _slice(data, direction):
        if direction in 'FL':
            return data[0:len(data) // 2]
        elif direction in 'BR':
            return data[len(data) // 2:]
        else:
            raise RuntimeError('Invalid direction')

    @staticmethod
    def _reduce(data, directions):
        for direction in directions:
            data = Seat._slice(data, direction)
        return data[0]

    @property
    def row(self):
        return self._reduce(range(128), self._rows)

    @property
    def column(self):
        return self._reduce(range(8), self._columns)

    @property
    def number(self):
        return self.row * 8 + self.column

    @classmethod
    def seats(cls, text):
        for line in text.splitlines():
            yield cls(line)


def part1(text):
    return [seat.number for seat in Seat.seats(text)]


def part2(text):
    seats = part1(text)
    missing = set(range(min(seats), max(seats))).difference(seats)
    return missing.pop()
