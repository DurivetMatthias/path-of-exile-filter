"""This file defines the rules for gems and items related to gems."""

import categories
import rule


class GemStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_GREEN


class Gem(GemStyle):
    def filter(self):
        return f"""
            BaseType "{self.name}"
        """


class SuperiorGem(GemStyle):
    def __init__(self, quality: str = "> 0", **kwargs):
        super().__init__(**kwargs)
        self.quality = quality

    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                GemQualityType "Superior"
                Quality {self.quality}
            """

        return f"""
            GemQualityType "Superior"
            Quality {self.quality}
        """


class AlternativeQualityGem(GemStyle):
    def __init__(self, quality: str = "> 0", **kwargs):
        super().__init__(**kwargs)
        self.quality = quality

    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                GemQualityType "Divergent" "Anomalous" "Phantasmal"
                Quality {self.quality}
            """

        return f"""
            GemQualityType "Divergent" "Anomalous" "Phantasmal"
            Quality {self.quality}
        """


class LeveledGem(GemStyle):
    def __init__(self, level: str, **kwargs):
        super().__init__(**kwargs)
        self.level = level

    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                GemLevel {self.level}
            """
        return f"""
            GemLevel {self.level}
        """


class HideGems(rule.Rule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, hide=True)

    def filter(self):
        return """
            Class "Gems"
        """


fire_gems = [
    "Burning Arrow",
    "Explosive Trap",
    "Fireball",
    "Molten Strike",
    "Purifying Flame",
    "Rolling Magma",
    "Detonate Dead",
    "Flame Wall",
    "Holy Flame Totem",
    "Molten Shell",
    "Summon Raging Spirit",
    "Bodyswap",
    "Flame Dash",
    "Blazing Salvo",
    "Elemental Hit",
    "Fire Trap",
    "Flame Surge",
    "Incinerate",
    "Infernal Blow",
    "Scorching Ray",
    "Searing Bond",
    "Volatile Dead",
    "Volcanic Fissure",
    "Herald of Ash",
    "Righteous Fire",
    "Wave of Conviction",
    "Alchemist's Mark",
    "Anger",
    "Flammability",
    "Infernal Cry",
    "Purity of Fire",
    "Armageddon Brand",
    "Artillery Ballista",
    "Blast Rain",
    "Consecrated Path",
    "Cremation",
    "Discharge",
    "Explosive Arrow",
    "Explosive Concoction",
    "Firestorm",
    "Flameblast",
    "Flamethrower Trap",
    "Pyroclast Mine",
    "Tectonic Slam",
    "Wild Strike",
    "Flame Link",
    "Summon Flame Golem",
]

rules = [
    Gem(
        name="Empower",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Gem(
        name="Enhance",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Gem(
        name="Enlighten",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Gem(
        name="Awakened",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Gem(
        name="Prime Regrading Lens",
        rarity=categories.RARITY.LEGENDARY,
    ),
    Gem(
        name="Secondary Regrading Lens",
        rarity=categories.RARITY.LEGENDARY,
    ),
    AlternativeQualityGem(
        rarity=categories.RARITY.LEGENDARY,
    ),
    LeveledGem(
        rarity=categories.RARITY.EPIC,
        level="> 20",
    ),
    *[
        LeveledGem(
            name=gem,
            rarity=categories.RARITY.RARE,
            level=">= 20",
            strictness=categories.STRICTNESS.STRICT,
        )
        for gem in fire_gems
    ],
    *[
        SuperiorGem(
            name=gem,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.STRICT,
        )
        for gem in fire_gems
    ],
    HideGems(),
]
