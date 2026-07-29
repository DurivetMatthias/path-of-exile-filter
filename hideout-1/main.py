from floors import cover_nebula, oriath_ground
from required import *
from hideout import Hideout
from doodad import place

floors = cover_nebula(oriath_ground)
hideout = Hideout(
    [
        place(STASH, 400, 250),
        place(WAYPOINT, 400, 200),
        place(CRAFTING_BENCH, 400, 300),
        place(MAP_DEVICE, 400, 400),
        place(HARVEST_BENCH, 400, 500),
        place(HEIST_STASH, 500, 250),
        place(EXPEDITION_STASH, 500, 200),
        place(RELIC_STASH, 500, 300),
        place(RECOMBINATOR, 500, 400),
        place(BREACH_STASH, 250, 250),
        place(MERCENARY_1, 200, 250),
        place(MERCENARY_2, 300, 250),
        place(MERCENARY_3, 400, 250),
        place(HELENA, 250, 500),
        place(KIRAC, 200, 250),
        place(DANNIG, 200, 200),
        place(GEWENNEN, 200, 300),
        place(TUJEN, 200, 400),
        place(ROG, 200, 500),
        place(LILLY, 300, 250),
        place(JOHAN, 300, 200),
        place(FAUSTUS, 300, 300),
        place(EAGON, 300, 400),
        place(AILITH, 300, 350),
        place(JUN, 350, 350),
        *floors,
    ]
)
hideout.generate("city")

# TODO geometrical layouts: rectangle, square, line
