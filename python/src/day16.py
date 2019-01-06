#!/usr/bin/env python
import json

from typing import NamedTuple, List


class Sample(NamedTuple):
    before: List[int]
    operation: List[int]
    after: List[int]

    @property
    def opid(self):
        return self.operation[0]

    @property
    def arguments(self):
        return self.operation[1:]


def parse(data):
    samples = []
    lines = iter(data.splitlines())

    line = next(lines)
    while line.startswith('Before:'):
        samples.append(
            Sample(
                json.loads(line[8:]),
                [int(n) for n in next(lines).split()],
                json.loads(next(lines)[8:]),
            )
        )
        next(lines)  # skip blank
        line = next(lines)

    program = [[int(n) for n in line.split()] for line in lines if line]
    return samples, program


class Computer:
    opcodes = {
        'addr': lambda r, a, b: r[a] + r[b],
        'addi': lambda r, a, b: r[a] + b,
        'mulr': lambda r, a, b: r[a] * r[b],
        'muli': lambda r, a, b: r[a] * b,
        'banr': lambda r, a, b: r[a] & r[b],
        'bani': lambda r, a, b: r[a] & b,
        'borr': lambda r, a, b: r[a] | r[b],
        'bori': lambda r, a, b: r[a] | b,
        'setr': lambda r, a, b: r[a],
        'seti': lambda r, a, b: a,
        'gtir': lambda r, a, b: int(a > r[b]),
        'gtri': lambda r, a, b: int(r[a] > b),
        'gtrr': lambda r, a, b: int(r[a] > r[b]),
        'eqir': lambda r, a, b: int(a == r[b]),
        'eqri': lambda r, a, b: int(r[a] == b),
        'eqrr': lambda r, a, b: int(r[a] == r[b]),
    }

    by_id = {}

    def __init__(self, initial=None):
        self.registers = [0, 0, 0, 0]
        self._initial = initial
        self.reset()

    def __getattr__(self, attr):
        if attr not in self.opcodes:
            name = self.__class__.__name__
            raise AttributeError(f"'{name}' object has no attribute '{attr}'")

        def wrapper(a, b, c):
            self.registers[c] = self.opcodes[attr](self.registers, a, b)
        return wrapper

    def reset(self):
        if self._initial is not None:
            self.registers = self._initial[:]

    def load(self, values):
        self._initial = values
        self.reset()


def part1(data):
    computer = Computer()
    samples, _ = parse(data)
    count = 0

    for sample in samples:
        matching = set()
        computer.load(sample.before)
        for opcode in Computer.opcodes:
            getattr(computer, opcode)(*sample.arguments)
            if computer.registers == sample.after:
                matching.add(opcode)
            computer.reset()

        if len(matching) >= 3:
            count += 1

    return count


def part2(data):
    samples, program = parse(data)
    computer = Computer()
    opcodes = list(Computer.opcodes)

    for sample in samples:
        matching = set()
        computer.load(sample.before)
        for opcode in opcodes:
            getattr(computer, opcode)(*sample.arguments)
            if computer.registers == sample.after:
                matching.add(opcode)
            computer.reset()

        if len(matching) == 1:
            opcode = matching.pop()
            Computer.by_id[sample.opid] = opcode
            opcodes.remove(opcode)

    computer.load([0, 0, 0, 0])
    for op, a, b, c in program:
        getattr(computer, Computer.by_id[op])(a, b, c)

    return computer.registers[0]
