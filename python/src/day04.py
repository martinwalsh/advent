#!/usr/bin/env python
from datetime import datetime
from collections import defaultdict, Counter


def parse_events(events):
    for event in sorted(events):
        yield datetime.strptime(event[1:17], '%Y-%m-%d %H:%M'), event[19:]


def analyze(events):
    guards = defaultdict(Counter)
    events = parse_events(events)

    for dt, event in events:
        if 'begins shift' in event:
            guard = int(event.split()[1][1:])
        elif event == 'falls asleep':
            start = dt
        elif event == 'wakes up':
            guards[guard].update(range(start.minute, dt.minute))
        else:
            raise ValueError(f'Invalid log input: {dt} {event}')

    return guards


def solve(events, func):
    guards = analyze(events)
    guard, minutes = max(guards.items(), key=func)
    return guard * minutes.most_common(1)[0][0]


def part1(events):
    def most_minutes(item):
        guard, minutes = item
        return sum(minutes.values())
    return solve(events, most_minutes)


def part2(events):
    def best_minute(item):
        guard, minutes = item
        return minutes.most_common(1)[0][1]
    return solve(events, best_minute)
