import json
from pathlib import Path

from app.item import Item
from app.markup import Markup

FILE_EXTENSION = "build"
FILTER_OUTPUT_PATH = (
    Path().home() / "Documents" / "my games" / "Path of Exile 2" / "BuildPlanner"
)
if not FILTER_OUTPUT_PATH.exists():
    FILTER_OUTPUT_PATH = Path(".")


class Passive:
    pass


class Skill:
    pass


class BuildFile:
    def __init__(
        self,
        *,
        name: Markup,
        description: Markup = "",
        ascendancy: str = "",
        passives: list[Passive] = [],
        skills: list[Skill] = [],
        items: list[Item] = [],
    ):
        self.name = name
        self.description = description
        self.ascendancy = ascendancy
        self.passives = passives
        self.skills = skills
        self.items = items

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "ascendancy": self.ascendancy,
            "inventory_slots": [item.to_dict() for item in self.items],
            "passives": [passive.to_dict() for passive in self.passives],
            "skills": [skill.to_dict() for skill in self.skills],
        }


def generate(name: str, build_file: BuildFile):
    output_filepath = FILTER_OUTPUT_PATH / f"{name}.{FILE_EXTENSION}"
    with open(output_filepath, mode="w", encoding="utf-8") as output_file:
        json.dump(build_file.to_dict(), output_file, indent=4)

    path_length = len(str(output_filepath))
    print("=" * path_length)
    print(output_filepath)
    print("=" * path_length)
