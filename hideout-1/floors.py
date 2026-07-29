from copy import copy
from itertools import product

from doodad import Doodad

oriath_ground = Doodad("Oriath Ground", 3123067737, version=5)


def cover_nebula(floor_doodad: Doodad) -> list[Doodad]:
    # Floors have size 46 units in both directions
    grid_points = [23 + index * 46 for index in range(9)]
    coordinates = product(grid_points, repeat=2)

    result = []
    for coordinate in coordinates:
        duplicate = copy(floor_doodad)
        floor_doodad.x = coordinate[0]
        floor_doodad.y = coordinate[1]
        result.append(duplicate)

    return result
