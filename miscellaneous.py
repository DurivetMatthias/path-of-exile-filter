import rule
import categories


class MiscStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.BLACK_ON_WHITE

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.DIAMOND


class MiscRule(MiscStyle):
    def __init__(self, class_name: str = "", **kwargs):
        super().__init__(**kwargs)
        self.class_name = class_name

    def filter(self):
        return f"""
            BaseType "{self.name}"
            Class "{self.class_name}"
        """


hidden = [
    "Incubator",
]

splinters = [
    "Splinter of Chayula",
    "Splinter of Esh",
    "Splinter of Tul",
    "Splinter of Uul-Netol",
    "Splinter of Xoph",
    "Timeless Eternal Empire Splinter",
    "Timeless Karui Splinter",
    "Timeless Maraketh Splinter",
    "Timeless Templar Splinter",
    "Timeless Vaal Splinter",
    "Simulacrum Splinter",
    "Ritual Splinter",
]

common = [
    *splinters,
    "Breachstone",
    "Stone of Passage",
    "Flashpowder Keg",
    "to the Goddess",
    "Exotic Coinage",
    "Scrap Metal",
    "Astragali",
    "Burial Medallion",
]
rare = [
    "Sacrifice at",
    "Mortal",
    "Vessel",
]
epic = [
    "Tainted",
    "Remnant of Corruption",
    "Resonator",
    "Scarab",
    "Catalyst",
    "Delirium Orb",
    "Report",
    "Lifeforce",
]
legendary = [
    "Invitation",
    "Blessing of",
    "Fragment of",
    "Emblem",
    "Breachstone",
    "Sacred Blossom",
    "Simulacrum",
    "Logbook",
    "Voidstone",
    "Memory",
    "Reliquary Key",
]

rules = [
    MiscRule(
        name="Oil",
        rarity=categories.RARITY.EPIC,
        class_name="Stackable Currency",
    ),
    MiscRule(
        name="Fossil",
        rarity=categories.RARITY.EPIC,
        class_name="Stackable Currency",
    ),
    MiscRule(
        name="Crest",
        rarity=categories.RARITY.EPIC,
        class_name="Map Fragments",
    ),
    MiscRule(
        name="Offering to the goddess",
        rarity=categories.RARITY.COMMON,
        strictness=categories.STRICTNESS.LESS_STRICT,
    ),
    *[
        MiscRule(
            name=item_name,
            hide=True,
        )
        for item_name in hidden
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=categories.RARITY.COMMON,
        )
        for item_name in common
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=categories.RARITY.RARE,
        )
        for item_name in rare
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=categories.RARITY.EPIC,
        )
        for item_name in epic
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=categories.RARITY.LEGENDARY,
        )
        for item_name in legendary
    ],
]
