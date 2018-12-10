#!/usr/bin/env python


class Node(object):
    def __init__(self, children, metadata):
        self._children = children
        self._metadata = metadata

    @property
    def metadata(self):
        metadata = self._metadata[:]
        for child in self._children:
            metadata.extend(child.metadata)
        return metadata

    @property
    def value(self):
        if self._children:
            return sum(
                self._children[n-1].value
                    for n in self._metadata if 0 <= n-1 < len(self._children)  # noqa
            )
        else:
            return sum(self._metadata)

    @classmethod
    def from_iter(cls, it):
        ccount, mcount = next(it), next(it)
        children = []
        for n in range(ccount):
            children.append(cls.from_iter(it))
        metadata = []
        for n in range(mcount):
            metadata.append(next(it))
        return cls(children, metadata)

    @classmethod
    def from_records(cls, records):
        return cls.from_iter(map(int, records))


def part1(data):
    return sum(Node.from_records(data.split()).metadata)


def part2(data):
    return Node.from_records(data.split()).value
