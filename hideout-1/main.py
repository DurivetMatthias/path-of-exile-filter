from floors import *
from required import *
from hideout import Hideout
from doodad import place
from geometry import place_in_shape, Circle, Point

floors = [
    *cover_nebula(wood_ground),
    *cover_nebula(water_low_ground),
]
center = Point(350, 350)
hideout = Hideout(
    [
        place(HELENA, center.x + 35, center.y - 20),
        place(STASH, center.x + 30, center.y - 40),
        place(MAP_DEVICE, center.x, center.y),
        place(MERCENARY_1, 170, 170),
        place(MERCENARY_2, 170, 170),
        place(MERCENARY_3, 170, 170),
        *place_in_shape(
            Circle(center.x, center.y, 150),
            [
                WAYPOINT,
                CRAFTING_BENCH,
                HARVEST_BENCH,
                HEIST_STASH,
                EXPEDITION_STASH,
                RELIC_STASH,
                RECOMBINATOR,
                BREACH_STASH,
                LILLY,
                KIRAC,
                DANNIG,
                GEWENNEN,
                TUJEN,
                JOHAN,
                FAUSTUS,
                EAGON,
                JUN,
                ROG,
            ],
        ),
        *floors,
    ]
)
hideout.generate("ship")

# TODO geometrical layouts: rectangle, square, line
