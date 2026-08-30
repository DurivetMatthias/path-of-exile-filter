from app.markup import Markup


class Passive:
    def __init__(
        self,
        id: str,
        level_interval: list[int] = [0, 100],
        *,
        weapon_set: int = None,
        additional_text: Markup = "",
    ):
        self.id = id
        self.weapon_set = weapon_set
        self.level_interval = level_interval
        self.additional_text = additional_text

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "weapon_set": self.weapon_set,
            "level_interval": self.level_interval,
            "additional_text": self.additional_text,
        }
