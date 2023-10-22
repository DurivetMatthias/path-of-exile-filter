"""This file defines the rules for item bases with uncommon properties."""

import categories
import rule


class AlteredStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_PINK

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.STAR


class FracturedItem(AlteredStyle):
    def filter(self):
        return """
            FracturedItem True
        """


class InfluencedItem(AlteredStyle):
    def filter(self):
        return """
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


class SynthesizedItem(AlteredStyle):
    def filter(self):
        return """
            SynthesisedItem True
        """


class EightySixItem(AlteredStyle):
    def filter(self):
        return """
            ItemLevel >= 86
        """


class WhiteWeapon(AlteredStyle):
    def filter(self):
        return """
            Class "One Hand Axes" "Daggers" "Claws" "One Hand Swords" "One Hand Maces" "Wands"
            Sockets 3W
        """


rules = [
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
