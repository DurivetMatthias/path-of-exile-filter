import math
from doodad import Doodad, place


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


base_rotation = -math.pi * 9 / 12


def get_circle_points(x, y, radius, amount) -> list[Point]:
    return [
        Point(
            x + radius * math.cos(2 * math.pi * i / amount + base_rotation),
            y + radius * math.sin(2 * math.pi * i / amount + base_rotation),
        )
        for i in range(amount)
    ]


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


def place_in_shape(shape: Circle, doodads: list[Doodad]):
    result = []
    amount = len(doodads)
    for index, point in enumerate(
        get_circle_points(shape.x, shape.y, shape.radius, amount)
    ):
        doodad = doodads[index]
        result.append(place(doodad, point.x, point.y))
    return result
