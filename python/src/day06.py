#!/usr/bin/env python


def part1(text):
    total = 0
    for group in text.split('\n\n'):
        yes = set()
        for answer in group.replace('\n', ''):
            yes.add(answer)
        total += len(yes)
    return total


def part2(text):
    total = 0
    for group in text.split('\n\n'):
        yes = set()
        for idx, person in enumerate(group.splitlines()):
            if idx == 0:
                yes = set(person)
            else:
                yes = yes.intersection(person)
        total += len(yes)
    return total
