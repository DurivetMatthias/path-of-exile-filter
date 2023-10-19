"""
This file describes item bases that have been altered in some way.
Typically these item bases are fairly rare.
"""

import categories

from rule import Rule


class AlteredItem(Rule):
    def label(self) -> str:
        """White text on purple background"""
        return """
            SetFontSize 45
            SetTextColor 255 255 255
            SetBackgroundColor 150 40 180
            SetBorderColor 150 40 180
        """

    def sound(self) -> categories.SOUND:
        return categories.SOUND.LILY_OOH

    def icon_color(self) -> categories.COLOR:
        return categories.COLOR.PURPLE

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.STAR


class FracturedItem(AlteredItem):
    def filter(self):
        return """
            FracturedItem True
        """


class InfluencedItem(AlteredItem):
    def filter(self):
        return """
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


class SynthesizedItem(AlteredItem):
    def filter(self):
        return """
            SynthesisedItem True
        """


class EightySixItem(AlteredItem):
    def filter(self):
        return """
            ItemLevel >= 86
        """


class WhiteWeapon(AlteredItem):
    def filter(self):
        return """
            Class "One Hand Axes" "Daggers" "Claws" "One Hand Swords" "One Hand Maces" "Wands"
            Sockets 3W
        """


rules = [
    FracturedItem(rarity=categories.RARITY.EPIC),
    InfluencedItem(rarity=categories.RARITY.EPIC),
    SynthesizedItem(rarity=categories.RARITY.EPIC),
    EightySixItem(rarity=categories.RARITY.EPIC),
    WhiteWeapon(rarity=categories.RARITY.EPIC),
]
