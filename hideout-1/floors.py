from copy import copy
from itertools import product

from doodad import Doodad

oriath_ground = Doodad("Oriath Ground", 3123067737, version=5)


def cover_nebula(floor_doodad: Doodad) -> list[Doodad]:
    # Floors have size 46 units in both directions
    # The Nebula hideout starts in the bottom corner at 170,170
    # The Nebula hideout ends at the top corner at 538,538
    # The left corner is 170, 538. The right corner is 538, 170
    grid_points = [170 + index * 46 for index in range(9)]
    coordinates = product(grid_points, repeat=2)

    result = []
    for coordinate in coordinates:
        duplicate = copy(floor_doodad)
        duplicate.x = coordinate[0]
        duplicate.y = coordinate[1]
        result.append(duplicate)

    return result
