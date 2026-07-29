from copy import copy


class Doodad:
    def __init__(
        self,
        name: str,
        hash: int,
        *,
        x: int = 0,
        y: int = 0,
        rotation: int = 0,
        version: int = 0,
    ):
        self.name = name
        self.hash = hash
        self.x = x
        self.y = y
        self.rotation = rotation
        self.version = version

    def to_dict(self) -> str:
        return {
            "name": self.name,
            "hash": self.hash,
            "x": self.x,
            "y": self.y,
            "rotation": self.rotation,
            "version": self.version,
        }


def place(doodad: Doodad, x, y, *, rotation=None, version=None) -> Doodad:
    instance = copy(doodad)

    instance.x = x
    instance.y = y

    if rotation is not None:
        instance.rotation = rotation
    if version is not None:
        instance.version = version

    return instance
