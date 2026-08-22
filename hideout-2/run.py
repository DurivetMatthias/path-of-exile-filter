from floors import *
from required import *
from hideout import *
from doodad import *
from geometry import *
from composite import *

floors = []
center = Point(400, 400)
hideout = Hideout(
    [
        place(
            MAP_DEVICE,
            center.x,
            center.y,
        ),
        *stash_group(center.x - 50, center.y - 50),
        *place_in_shape(
            Circle(center.x, center.y, 125),
            [
                version(WAYPOINT, 2),
                RELIC_STASH,
                REFORGE,
                SALVAGE,
                version(WELL, 1),
                WARDROBE,
                ANGE,
                ZELINA,
                ALVA,
                JADO,
                HILDA,
                VERISIUM_ANVIL,
                FARROW,
            ],
        ),
        *floors,
    ]
)
hideout.generate("alpine")
