#!/usr/bin/env python
from itertools import cycle
from collections import Counter


class Marble(object):
    def __init__(self, value):
        self.value = value
        self.prev = self.next = self

    def insert(self, other):
        other.next = self
        other.prev = self.prev
        other.prev.next = other
        self.prev = other
        return other

    def pop(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        return self, self.next


def solve(num_players, num_marbles):
    scores = Counter()
    current = Marble(0)

    for player, number in \
            zip(cycle(range(1, num_players + 1)), range(1, num_marbles + 1)):
        if number % 23 == 0:
            for n in range(7):
                current = current.prev
            marble, current = current.pop()
            scores[player] += marble.value + number
        else:
            for n in range(2):
                current = current.next
            current = current.insert(Marble(number))

    return scores.most_common(1)[0][1]
