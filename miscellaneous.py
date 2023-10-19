from rule import Rule
import rarity_options


class MiscStyle(Rule):
    def label(self) -> str:
        """White text on a black background"""
        return """
            SetFontSize 45
            SetTextColor 255 255 255
            SetBackgroundColor 0 0 0
            SetBorderColor 0 0 0
        """

    def sound(self) -> str:
        return """
            DisableDropSound
        """


class MiscRule(MiscStyle):
    def filter(self):
        return f"""
            BaseType "{self.name}"
        """


hidden = [
    "Incubator",
    "Simulacrum Splinter",
]
common = [
    "Splinter",
    "Breachstone",
    "Stone of Passage",
    "Flashpowder Keg",
]
rare = [
    "Fragment",
    "Exotic Coinage",
    "Scrap Metal",
    "Astragali",
    "Burial Medallion",
    "Vessel",
    "Oil",
    "Catalyst",
    "Delirium Orb",
    "Fossil",
    "Report",
    "Lifeforce",
]
epic = [
    "Tainted",
    "Essence",
    "Remnant of Corruption",
    "Resonator",
    "Scarab",
    "Invitation",
]
legendary = [
    "Crest",
    "Blessing of",
    "Emblem",
    "Sacred Blossom",
    "Simulacrum",
    "Logbook",
    "Voidstone",
    "Memory",
    "Reliquary Key",
]

rules = [
    *[
        MiscRule(
            name=item_name,
            rarity=rarity_options.COMMON,
            hide=True,
        )
        for item_name in hidden
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=rarity_options.COMMON,
        )
        for item_name in common
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=rarity_options.RARE,
        )
        for item_name in rare
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=rarity_options.EPIC,
        )
        for item_name in epic
    ],
    *[
        MiscRule(
            name=item_name,
            rarity=rarity_options.LEGENDARY,
        )
        for item_name in legendary
    ],
]
