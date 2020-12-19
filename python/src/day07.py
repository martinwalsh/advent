#!/usr/bin/env python
import re


class Bag:
    _bags = {}

    def __init__(self, name):
        self.name = name
        self.edges = {
            'parents': {},
            'children': {},
        }

    def add_edge(self, name, weight, edge_type='children'):
        node = self.get(name)
        if name not in self.edges[edge_type]:
            self.edges[edge_type][name] = {
                'node': node,
                'weight': weight,
            }
        return node

    def _traverse(self, edge_type):
        visited = set()

        edges = list(self.edges[edge_type].items())
        while edges:
            name, edge = edges.pop(0)
            yield name, edge['node'], edge['weight']

            for name, data in edge['node'].edges[edge_type].items():
                if name not in visited:
                    edges.append((name, data))
            visited.add(name)

    @property
    def parents(self):
        return set(name for name, _, _ in self._traverse('parents'))

    @property
    def children(self):
        for _, attrs in self.edges['children'].items():
            yield (attrs['node'], attrs['weight'])

    @property
    def bags(self):
        count = 0
        for node, weight in self.children:
            count += weight + weight * node.bags
        return count

    @classmethod
    def get(cls, name):
        if name not in cls._bags:
            cls._bags[name] = cls(name)
        return cls._bags[name]

    @classmethod
    def reset(cls):
        cls._bags = {}

    def __repr__(self):
        return '<{} | {} | {}>'.format(
            self.name,
            repr(list(self.edges['children'])),
            repr(list(self.edges['parents'])),
        )


class Graph:
    _patterns = {
        'edge': re.compile(r'^(?P<name>\w+ \w+) bags contain (?P<adjacents>.*)\.$'),
        'adjacents': re.compile(r'(?P<count>\d+) (?P<name>\w+ \w+) bags?'),
    }

    def __init__(self, bags):
        self.bags = bags

    def get(self, name):
        return self.bags.get(name)

    @classmethod
    def parse(cls, text):
        Bag.reset()

        bags = {}
        for line in text.splitlines():
            spec = cls._patterns['edge'].search(line)
            bag = Bag.get(spec.group('name'))

            children = cls._patterns['adjacents'].findall(spec.group('adjacents'))
            for weight, name in children:
                child = bag.add_edge(name, int(weight))
                child.add_edge(bag.name, int(weight), 'parents')

            bags[bag.name] = bag
        return cls(bags)


def part1(text):
    return len(Graph.parse(text).get('shiny gold').parents)


def part2(text):
    return Graph.parse(text).get('shiny gold').bags
