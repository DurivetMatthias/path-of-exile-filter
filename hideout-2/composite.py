from doodad import *
from required import *
from geometry import *


def stash_group(x, y) -> list[Doodad]:
    result = [
        place(DORYANI, x + 10, y - 10),
        place(STASH, x, y, rotation=57500),
        place(ZOLIN, x - 10, y + 10),
    ]
    return result
