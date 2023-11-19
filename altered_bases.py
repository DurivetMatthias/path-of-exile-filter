"""This file defines the rules for item bases with uncommon properties."""

import categories
import rule


class AlteredStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_PINK

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.STAR


class CorruptedImplicitItem(AlteredStyle):
    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                CorruptedMods > 0
            """
        return """
            CorruptedMods > 0
        """


class FracturedItem(AlteredStyle):
    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                FracturedItem True
            """
        return """
            FracturedItem True
        """


class InfluencedItem(AlteredStyle):
    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
            """
        return """
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


class SynthesizedItem(AlteredStyle):
    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                SynthesisedItem True
            """
        return """
            SynthesisedItem True
        """


class EightySixItem(AlteredStyle):
    def filter(self):
        if self.name:
            return f"""
                BaseType "{self.name}"
                ItemLevel >= 86
            """
        return """
            ItemLevel >= 86
        """


class WhiteWeapon(AlteredStyle):
    def filter(self):
        return """
            Class "One Hand Axes" "Daggers" "Claws" "One Hand Swords" "One Hand Maces" "Wands"
            Sockets 3W
        """


jewels = [
    "Crimson Jewel",
    "Viridian Jewel",
    "Cobalt Jewel",
]

rules = [
    *[
        FracturedItem(
            name=jewel,
            rarity=categories.RARITY.EPIC,
        )
        for jewel in jewels
    ],
    *[
        CorruptedImplicitItem(
            name=jewel,
            rarity=categories.RARITY.EPIC,
        )
        for jewel in jewels
    ],
    FracturedItem(
        rarity=categories.RARITY.EPIC,
        strictness=categories.STRICTNESS.STRICT,
    ),
    InfluencedItem(
        rarity=categories.RARITY.EPIC,
        strictness=categories.STRICTNESS.STRICT,
    ),
    SynthesizedItem(
        rarity=categories.RARITY.EPIC,
        strictness=categories.STRICTNESS.STRICT,
    ),
    EightySixItem(
        rarity=categories.RARITY.EPIC,
        strictness=categories.STRICTNESS.STRICT,
    ),
    WhiteWeapon(
        rarity=categories.RARITY.EPIC,
        strictness=categories.STRICTNESS.LESS_STRICT,
    ),
]
