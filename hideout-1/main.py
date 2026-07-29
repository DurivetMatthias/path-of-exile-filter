from floors import cover_nebula, oriath_ground
from hideout import Hideout

floors = cover_nebula(oriath_ground)
hideout = Hideout(
    [
        *floors,
    ]
)
hideout.generate("ship")
