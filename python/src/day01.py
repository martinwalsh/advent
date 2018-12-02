#!/usr/bin/env python


def calibrate(seq, freq=0):
    for item in seq:
        try:
            freq += int(item)
        except ValueError:
            raise ValueError('Invalid input item: {}'.format(item))
        else:
            yield freq


def part1(seq):
    return list(calibrate(seq))[-1]


def part2(seq, freq=0):
    seen = {freq}
    retries = 1000
    while retries:
        for freq in calibrate(seq, freq):
            if freq in seen:
                return freq
            seen.add(freq)
        retries -= 1
    raise ValueError('Invalid input: reached retry limit')
