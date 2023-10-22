import rule
import categories


class UniqueStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.ORANGE_ON_BLACK_WITH_BORDER

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.CROSS


class Unique(UniqueStyle):
    def filter(self):
        return f"""
            BaseType == "{self.name}"
            Rarity Unique
        """


class UniqueClass(UniqueStyle):
    def filter(self):
        return f"""
            Class == "{self.name}"
            Rarity Unique
        """


rules = [
    Unique(
        name="Leather Belt",
        rarity=categories.RARITY.EPIC,
    ),
    Unique(
        name="Wyrmscale Boots",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Unique(
        name="Onyx Amulet",
        rarity=categories.RARITY.LEGENDARY,
    ),
    UniqueClass(
        name="Jewels",
        rarity=categories.RARITY.LEGENDARY,
    ),
    UniqueClass(
        name="Maps",
        rarity=categories.RARITY.LEGENDARY,
    ),
]
