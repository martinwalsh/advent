#!/usr/bin/env python


class Location:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def point(self):
        return (self.x, self.y)

    @property
    def distance(self):
        return abs(self.x) + abs(self.y)


class Base:
    def __init__(self, instructions):
        self.instructions = instructions
        self.reset()

    def reset(self):
        self.direction = 90  # East
        self.location = Location(0, 0)

    def navigate(self):
        for operation, value in self.instructions:
            getattr(self, f'do_{operation}')(value)

    @classmethod
    def parse(cls, text):
        return cls([(i[:1], int(i[1:])) for i in text.splitlines()])


class Ship(Base):
    def do_N(self, value):
        self.location.y -= value

    def do_S(self, value):
        self.location.y += value

    def do_E(self, value):
        self.location.x += value

    def do_W(self, value):
        self.location.x -= value

    def _rotate(self, count, rotation):
        for _ in range(count):
            self.direction = (self.direction + rotation) % 360

    def do_L(self, value):
        assert value % 90 == 0
        self._rotate(value // 90, -90)

    def do_R(self, value):
        assert value % 90 == 0
        self._rotate(value // 90, 90)

    def do_F(self, value):
        dispatch = {
            0: self.do_N,
            90: self.do_E,
            180: self.do_S,
            270: self.do_W,
        }
        dispatch[self.direction](value)


class ShipWithWaypoint(Base):
    def __init__(self, instructions):
        super().__init__(instructions)

    def reset(self):
        super().reset()
        self.waypoint = Location(10, -1)

    def do_N(self, value):
        self.waypoint.y -= value

    def do_S(self, value):
        self.waypoint.y += value

    def do_E(self, value):
        self.waypoint.x += value

    def do_W(self, value):
        self.waypoint.x -= value

    def do_L(self, value):
        for _ in range(value // 90):
            self.direction = (self.direction - 90) % 360
            self.waypoint.x, self.waypoint.y = (
                self.waypoint.y - self.location.y + self.location.x,
                -(self.waypoint.x - self.location.x) + self.location.y
            )

    def do_R(self, value):
        for _ in range(value // 90):
            self.direction = (self.direction + 90) % 360
            self.waypoint.x, self.waypoint.y = (
                -(self.waypoint.y - self.location.y) + self.location.x,
                self.waypoint.x - self.location.x + self.location.y
            )

    @staticmethod
    def _converge(p1, p2):
        delta_x, delta_y = (p1.x - p2.x, p1.y - p2.y)
        p1.x += delta_x
        p2.x += delta_x
        p1.y += delta_y
        p2.y += delta_y

    def do_F(self, value):
        for _ in range(value):
            self._converge(self.waypoint, self.location)


def part1(text):
    ship = Ship.parse(text)
    ship.navigate()
    return ship.location.distance


def part2(text):
    ship = ShipWithWaypoint.parse(text)
    ship.navigate()
    return ship.location.distance
