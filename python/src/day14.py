#!/usr/bin/env python


def stringify(l):
    return ''.join(str(n) for n in l)


def part1(minimum):
    queue = [3, 7]
    elves = [0, 1]
    while len(queue) < minimum + 10:
        total = sum(queue[i] for i in elves)
        queue.extend(map(int, str(total)))
        elves = [(e + queue[e] + 1) % len(queue) for e in elves]
    return stringify(queue[minimum:minimum+10])


class Elf:
    def __init__(self, queue, position):
        self.queue = queue
        self.position = position

    @property
    def value(self):
        return self.queue[self.position]

    def step(self):
        self.position = (self.position + self.value + 1) % len(self.queue)

    def __add__(self, other):
        return map(int, str(self.value + other.value))


def part2(match):
    match = list(map(int, str(match)))
    queue = [3, 7]
    elf1 = Elf(queue, 0)
    elf2 = Elf(queue, 1)

    while True:
        for n in elf1 + elf2:
            queue.append(n)
            if queue[-len(match):] == match:
                return len(queue) - len(match)
        elf1.step()
        elf2.step()
