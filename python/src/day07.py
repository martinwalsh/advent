#!/usr/bin/env python
from pathlib import Path


class File:
    def __init__(self, name, size, cwd):
        self.name = name
        self.size = size
        self.path = cwd.join(name)


class Directory:
    def __init__(self, name, cwd=None):
        self.name = name
        self.path = Path("/") if cwd is None else cwd.join(name)

        self.parent = cwd
        self._children = []

    @property
    def size(self):
        return sum(child.size for child in self._children)

    def add(self, dir_or_file):
        if dir_or_file not in self._children:
            self._children.append(dir_or_file)

    def join(self, name):
        return self.path.joinpath(name)


def parse(data):
    root = cwd = Directory("")
    directories = {root.path: root}
    for line in data.splitlines():
        if line.startswith("$ cd"):
            *_, basename = line.split()
            if basename == "..":
                cwd = cwd.parent
            else:
                d = Directory(basename, cwd)
                if d.path in directories:
                    d = directories[d.path]
                else:
                    cwd.add(d)
                cwd = d
            directories.update({cwd.path: cwd})

        size, *r = line.split()
        if size.isnumeric():
            cwd.add(File(r[0], int(size), cwd))

    return directories


def part1(data):
    return sum(d.size for d in parse(data).values() if d.size <= 100000)


def part2(data):
    directories = parse(data)
    disk_size = directories[Path("/")].size
    needed = 30000000 - (70000000 - disk_size)
    first, *_ = sorted([d.size for d in directories.values() if d.size >= needed])
    return first
