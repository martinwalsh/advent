#!/usr/bin/env python
import string

class Passport:
    _required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid') # 'cid'
    _delimiter = '\n\n'

    @staticmethod
    def _validate_hgt(value):
        value, unit = value[:-2], value[-2:]
        return unit in ('cm', 'in') and (
            150 <= int(value) <= 193 if unit == 'cm' else 59 <= int(value) <= 76
        )

    @staticmethod
    def _validate_hcl(value):
        return len(value) == 7 and all(c in (string.digits + string.ascii_lowercase + '#') for c in value)

    @staticmethod
    def _validate(field, value):
        validators = {
            'byr': lambda x: 1920 <= int(x) <= 2002,
            'iyr': lambda x: 2010 <= int(x) <= 2020,
            'eyr': lambda x: 2020 <= int(x) <= 2030,
            'hgt': Passport._validate_hgt,
            'hcl': Passport._validate_hcl,
            'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            'pid': lambda x: len(x) == 9 and x.isnumeric(),
            '_': lambda x: False,
        }
        return validators.get(field, validators['_'])(value)

    def __init__(self, text):
        self._data = self._parse(text)

    def _parse(self, text):
        data = {}
        for line in text.splitlines():
            for item in line.split():
                key, value = item.split(':')
                data[key] = value
        return data

    def validate(self, extra_validation=False):
        if extra_validation:
            return all(r in self._data for r in self._required) and \
                    all(self._validate(r, self._data[r]) for r in self._required)
        else:
            return all(r in self._data for r in self._required)

    @classmethod
    def parse(cls, text):
        return [cls(p) for p in text.split(cls._delimiter)]

    @classmethod
    def get_valid(cls, text, extra_validation=False):
        return [p for p in cls.parse(text) if p.validate(extra_validation)]


def part1(text):
    return len(Passport.get_valid(text))


def part2(text):
    return len(Passport.get_valid(text, True))
