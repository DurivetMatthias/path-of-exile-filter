from enum import StrEnum
from markup import Markup
from textwrap import dedent


class INVENTORY_SLOT(StrEnum):
    WEAPON = "Weapon1"
    OFFHAND = "Offhand1"
    RING1 = "Ring1"
    RING2 = "Ring2"
    RING3 = "Ring3"
    AMULET = "Amulet1"
    BELT = "Belt1"
    HELMET = "Helmet1"
    GLOVES = "Gloves1"
    BOOTS = "Boots1"
    BODY = "BodyArmour1"


class Item:
    def __init__(
        self,
        inventory_id: INVENTORY_SLOT,
        additional_text: Markup = "",
        level_interval: list[int] = [0, 100],
        *,
        slot_x: int = 0,
        slot_y: int = 0,
        unique_name: str = "",
    ):
        self.inventory_id = inventory_id
        self.slot_x = slot_x
        self.slot_y = slot_y
        self.level_interval = level_interval
        self.unique_name = unique_name
        self.additional_text = dedent(additional_text).strip()

    def to_dict(self) -> dict:
        return {
            "inventory_id": self.inventory_id,
            "slot_x": self.slot_x,
            "slot_y": self.slot_y,
            "level_interval": self.level_interval,
            "unique_name": self.unique_name,
            "additional_text": self.additional_text,
        }
