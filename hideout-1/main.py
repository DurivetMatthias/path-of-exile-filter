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
        place(
            MAP_DEVICE,
            center.x,
            center.y,
            rotation=16000,
        ),
        place(MERCENARY_1, 170, 170),
        place(MERCENARY_2, 170, 170),
        place(MERCENARY_3, 170, 170),
        *place_in_shape(
            Circle(center.x, center.y, 50),
            [
                WAYPOINT,
                CRAFTING_BENCH,
                STASH,
                HELENA,
                RECOMBINATOR,
                HARVEST_BENCH,
                LILLY,
                KIRAC,
            ],
        ),
        *place_in_shape(
            Circle(center.x, center.y, 150),
            [
                HEIST_STASH,
                EXPEDITION_STASH,
                RELIC_STASH,
                BREACH_STASH,
                FAUSTUS,
                EAGON,
                JUN,
                JOHAN,
                DANNIG,
                GEWENNEN,
                ROG,
                TUJEN,
            ],
        ),
        *floors,
    ]
)
hideout.generate("ship")

# TODO geometrical layouts: rectangle, square, line
