#!/usr/bin/env python
import re

def parse_line(line):
    return re.search(r'^(\d+)-(\d+) ([a-z]): (.*)$', line).groups()


def part1(text):
    valid_passwords = 0

    for line in text.strip().splitlines():
        _min, _max, letter, password = parse_line(line)
        count = password.count(letter)
        if int(_min) <= count <= int(_max):
            valid_passwords += 1

    return valid_passwords


def part2(text):
    valid_passwords = 0

    for line in text.strip().splitlines():
        pos1, pos2, letter, password = parse_line(line)
        pos1, pos2 = int(pos1) - 1, int(pos2) - 1
        if not (password[pos1] == letter and password[pos2] == letter) \
                and (password[pos1] == letter or password[pos2] == letter):
            valid_passwords += 1

    return valid_passwords
