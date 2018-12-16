#!/usr/bin/env python


def parse_input(lines):
    return (
        lines[0][15:],
        {k: v for k, v in (line.split(' => ') for line in lines[2:])}
    )


def fix_margins(planters, zero, pad='.....'):
    if planters.startswith(pad * 2):
        zero += len(pad)
        planters = planters[5:]

    if not planters.startswith(pad):
        zero -= len(pad)
        planters = pad + planters

    if planters.endswith(pad * 2):
        planters = planters[:-5]

    if not planters.endswith(pad):
        planters += pad

    return planters, zero


def get_next(planters, rules):
    result = planters[:2]
    for i in range(2, len(planters) - 1):
        result += rules.get(planters[i-2:i+3], '.')
    return result + planters[-2:]


def part1(data, generations=20):
    planters, rules = parse_input(data)

    zero = 0
    previous = ''
    for i in range(0, generations):
        planters, zero = fix_margins(planters, zero)
        if previous.strip('.') == planters.strip('.'):
            zero += generations - i
            break
        else:
            previous = planters
        planters = get_next(planters, rules)

    return sum(i for i, x in enumerate(planters, zero) if x == '#')


def part2(data, generations=50000000000):
    return part1(data, generations)
