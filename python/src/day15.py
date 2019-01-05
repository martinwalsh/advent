#!/usr/bin/env python
import sys

from collections import deque


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

        self.adjacent = []
        self.unit = None


class Unit:
    _units = None

    def __init__(self, val, node, power=3):
        self.val = val
        self.node = node
        self.power = power
        self.health = 200

    def move_to(self, node):
        node.unit = self
        self.node.unit = None
        node.val, self.node.val = self.node.val, node.val
        self.node = node

    def attack(self, enemy):
        enemy.health -= self.power

    @property
    def is_dead(self):
        return self.health <= 0

    def die(self):
        self.node.unit = None
        self.node.val = '.'
        self._units.remove(self)


class Battle:
    def __init__(self, data, elf_power=3):
        self._parse(data, elf_power)
        self.complete = False
        self.rounds = 0

    @property
    def score(self):
        return self.rounds * sum(u.health for u in self.units)

    def find_shortest_path(self, unit, endpoints):
        visited = set()
        endpoints = set(e.node for e in endpoints)

        queue = deque([(unit.node, [unit.node])])

        while queue:
            current, path = queue.popleft()
            if current not in visited:
                for node in current.adjacent:
                    if node in endpoints:
                        return path + [node]
                    else:
                        if node.val not in ['E', 'G']:
                            queue.append((node, path + [node]))
                visited.add(current)

    def round(self):
        for unit in sorted(self.units, key=lambda u: (u.node.y, u.node.x)):
            if unit.is_dead:
                continue

            enemies = [u for u in self.units if u.val != unit.val]

            if enemies:
                path = self.find_shortest_path(unit, enemies)

                if path and len(path) > 2:
                    # print(f'move: {unit} ---> {path[1]}')
                    unit.move_to(path[1])

                nearby = [n.unit for n in unit.node.adjacent if n.unit in enemies]
                # print(f'detecting nearby: {unit} --> {nearby}')
                if nearby:
                    target = min(nearby, key=lambda u: (u.health, u.node.y, u.node.x))
                    # print(f'attack: {unit} ---> {target}')
                    unit.attack(target)
                    if target.is_dead:
                        target.die()

            else:
                self.complete = True
                break
        else:
            self.rounds += 1

    def _parse(self, data, elf_power):
        nodes, units = {}, []
        for y, line in enumerate(data.splitlines()):
            for x, val in enumerate(line):
                node = Node(x, y, val)
                if val in ['E', 'G']:
                    unit = Unit(val, node, elf_power if val == 'E' else 3)
                    units.append(unit)
                    node.unit = unit
                nodes[(x, y)] = node

        self.xmax, self.ymax = x, y

        for (x, y), node in nodes.items():
            # add adjacent nodes in reading order
            for offset in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                coords = (x + offset[0], y + offset[1])
                if coords in nodes and nodes[coords].val != '#':
                    node.adjacent.append(nodes[coords])

        self.nodes = nodes
        self.units = Unit._units = units


def part1(data, elf_power=3):
    battle = Battle(data, elf_power)
    while not battle.complete:
        battle.round()
    return battle


def part2(data):
    def count_elves(units):
        return len([u for u in units if u.val == 'E'])

    battle = Battle(data)
    initial = count_elves(battle.units)

    for power in range(4, sys.maxsize):
        battle = part1(data, power)
        while not battle.complete:
            battle.round()

        if initial == count_elves(battle.units):
            break

    return battle, power
