#!/usr/bin/env python
from itertools import count
from collections import deque
from operator import attrgetter
from string import ascii_uppercase as uppercase


def extract(records):
    for record in records:
        yield record[5], record[36]


class Node(object):
    def __init__(self, name, step_duration=0):
        self.name = name
        self.children = set()
        self.parents = set()

        self.started = 0
        self.duration = step_duration + uppercase.index(name)

    def is_expired(self, seconds):
        return seconds - self.started >= self.duration

    @staticmethod
    def get_roots_from_records(records, step_duration):
        nodes = {}
        for a, b in extract(records):
            parent = nodes.setdefault(a, Node(a, step_duration))
            child = nodes.setdefault(b, Node(b, step_duration))
            child.parents.add(parent)
            parent.children.add(child)

        return {node for node in nodes.values() if not node.parents}


def traverse(records, step_duration=0):
    available = Node.get_roots_from_records(records, step_duration)
    complete = set()
    while available:
        node = min(available, key=attrgetter('name'))
        complete.add(node)
        available.remove(node)
        yield node

        for child in node.children:
            if all(n in complete for n in child.parents):
                available.add(child)


class DQ(deque):
    def expire(self, seconds):
        for item in self.copy():
            if item.is_expired(seconds):
                yield item
                self.remove(item)


def team_traverse(records, workers=2, step_duration=0):
    available = Node.get_roots_from_records(records, step_duration)
    complete = set()
    pending = DQ(maxlen=workers)

    for seconds in count():
        if not available and not pending:
            return seconds

        for node in sorted(available, key=attrgetter('name')):
            if len(pending) == workers:
                break
            node.started = seconds
            pending.append(node)
            available.remove(node)

        for node in pending.expire(seconds):
            complete.add(node)
            for child in node.children:
                if all(n in complete for n in child.parents):
                    available.add(child)


def part1(records):
    return ''.join(n.name for n in traverse(records))


def part2(records, workers=2, step_duration=0):
    return team_traverse(records, workers, step_duration)
