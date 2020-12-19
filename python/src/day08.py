#!/usr/bin/env python


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.finished = False

    def __iter__(self):
        pointer = accumulator = 0
        visited = set()
        while pointer not in visited:
            visited.add(pointer)

            try:
                operation, value = self.instructions[pointer]
            except IndexError:
                self.finished = True
                return

            pointer, accumulator = getattr(self, operation)(pointer, accumulator, value)

            yield accumulator

    @staticmethod
    def nop(pointer, accumulator, value):
        return pointer + 1, accumulator

    @staticmethod
    def acc(pointer, accumulator, value):
        return pointer + 1, accumulator + value

    @staticmethod
    def jmp(pointer, accumulator, value):
        return pointer + value, accumulator

    @staticmethod
    def parse(text):
        def split(instruction):
            operation, value = instruction.split()
            return (operation, int(value))
        return [split(instruction) for instruction in text.splitlines()]

    def accumulate(self):
        return list(self)[-1]

    @classmethod
    def find_corrupted_value(cls, text):
        return cls(cls.parse(text)).accumulate()

    @classmethod
    def find_fixed_value(cls, text):
        instructions = cls.parse(text)
        for idx, (operation, value) in enumerate(instructions):
            if operation == 'acc':
                continue

            _instructions = instructions[:]
            if operation == 'jmp':
                _instructions[idx] = ('nop', value)
            if operation == 'nop':
                _instructions[idx] = ('jmp', value)

            computer = cls(_instructions)
            accumulator = computer.accumulate()

            if computer.finished:
                return accumulator


def part1(text):
    return Computer.find_corrupted_value(text)


def part2(text):
    return Computer.find_fixed_value(text)
