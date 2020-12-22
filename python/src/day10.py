#!/usr/bin/env python
import networkx as nx

from functools import reduce
from collections import defaultdict


def parse(text):
    return sorted(int(n) for n in text.splitlines())


def get_deltas(adapters):
    adapters.append(max(adapters) + 3)

    tracker = defaultdict(int)

    def delta(x, y):
        tracker[y-x] += 1
        return y

    reduce(delta, adapters, 0)
    return tracker


def count_paths(adapters):
    g = nx.DiGraph()
    g.add_nodes_from(adapters)

    for adapter in adapters:
        for adjacent in (adapter + i for i in range(1, 4)):
            if adjacent in adapters:
                g.add_edge(adapter, adjacent)

    adjmat = nx.adjacency_matrix(g)
    return sum([
        (adjmat ** exp)[0, len(adapters)-1] for exp in range(2, len(adapters))
    ])


def part1(text):
    tracker = get_deltas(parse(text))
    return tracker[1] * tracker[3]


def part2(text):
    adapters = parse(text)
    adapters.insert(0, 0)
    adapters.append(max(adapters) + 3)
    return count_paths(adapters)
