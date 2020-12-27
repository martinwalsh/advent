#!/usr/bin/env python
from collections import defaultdict


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.memory = defaultdict(int)

    @property
    def mask(self):
        return [(pos, n) for pos, n in enumerate(self._mask) if n != 'X']

    @property
    def sum(self):
        return sum(self.memory.values())

    def do_set_mask(self, mask):
        self._mask = mask

    def do_store(self, address, value):
        self.memory[address] = int(self._apply_mask(value), 2)

    def _apply_mask(self, value):
        _bin = list(bin(value)[2:].zfill(36))
        for pos, n in self.mask:
            _bin[pos] = n
        return ''.join(_bin)

    def compute(self):
        for name, *args in self.instructions:
            getattr(self, name)(*args)

    @classmethod
    def parse(cls, text, part):
        instructions = []
        for line in text.splitlines():
            if line.startswith('mem'):
                address, value = [int(n) for n in line[4:].split('] = ')]
                instructions.append(('do_store', address, value))
            else:
                instructions.append(('do_set_mask', line[7:]))
        return cls(instructions)


class ComputerV2(Computer):
    @property
    def mask(self):
        return [(pos, n) for pos, n in enumerate(self._mask) if n != '0']

    @staticmethod
    def _replace(mask, replacement):
        replacement = iter(replacement)
        output = []
        for char in mask:
            if char == 'X':
                output.append(next(replacement))
            else:
                output.append(char)
        return ''.join(output)

    @staticmethod
    def _expand_mask(mask):
        if 'X' in mask:
            for replacement in range(int('1' * mask.count('X'), 2) + 1):
                replacement = bin(replacement)[2:].zfill(mask.count('X'))
                yield ComputerV2._replace(mask, replacement)
        else:
            yield mask

    def do_store(self, address, value):
        address = self._apply_mask(address)
        for address in self._expand_mask(address):
            self.memory[int(address, 2)] = value


def part1(text):
    computer = Computer.parse(text, 'part1')
    computer.compute()
    return computer.sum


def part2(text):
    computer = ComputerV2.parse(text, 'part2')
    computer.compute()
    return computer.sum
