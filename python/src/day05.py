#!/usr/bin/env python
import re

from collections import deque


def parse(data):
    stacks = []
    letters = re.compile(r"\[([A-Z])\]")
    instructions = re.compile(r"move (\d+) from (\d+) to (\d+)")

    lines = iter(data.splitlines())
    for line in lines:
        if letters.search(line) is None:
            break
        ncols = (len(line) + 1) // 4
        if not stacks:
            for _ in range(ncols):
                stacks.append(deque())
        for i in range(ncols):
            value = line[i * 4 + 1].strip()
            if value:
                stacks[i].insert(0, value)

    actions = []
    for line in lines:
        numbers = instructions.search(line)
        if numbers is not None:
            actions.append([int(n) for n in numbers.groups()])

    return stacks, actions


def part1(data):
    stacks, actions = parse(data)
    for count, frm, to in actions:
        for _ in range(count):
            stacks[to - 1].append(stacks[frm - 1].pop())
    return "".join(s.pop() for s in stacks)


def part2(data):
    stacks, actions = parse(data)
    for count, frm, to in actions:
        for item in reversed([stacks[frm - 1].pop() for _ in range(count)]):
            stacks[to - 1].append(item)
    return "".join(s.pop() for s in stacks)
