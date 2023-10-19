"""
Define filter rules as python classes.
Overwrite a method to alter how the rule behaves.
"""

from typing import Optional

import categories


class Rule:
    """Base class to define rules in an item filter file."""

    def __init__(
        self,
        name: Optional[str] = None,
        hide: bool = False,
        rarity: categories.RARITY = categories.RARITY.COMMON,
        strictness: categories.STRICTNESS = categories.STRICTNESS.MAX,
    ) -> None:
        """Initialise the rules and its properties"""
        self.name = name
        self.rarity = rarity
        self.hide = hide
        self.strictness = strictness

    def format(self, rules_block: str) -> str:
        """Format the final rules block to be human-readable"""
        lines = rules_block.splitlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line != ""]
        statement = lines.pop(0)
        lines = [4 * " " + line for line in lines]
        lines = [statement, *lines]
        result = "\n".join(lines)
        return "\n" + result + "\n"

    def filter(self):
        """Limit the rule to certain properties of the item"""
        return f'BaseType == "{self.name}"'

    def hidden(self):
        """Determines if this becomes a Hide or Show rule"""
        return self.hide

    def label(self) -> categories.LABEL:
        """Customize the look of the label that appears in-game"""
        return categories.LABEL.WHITE_ON_BLACK

    def icon(self) -> str:
        """Customize the look of the map icon that appears in-game"""
        color = self.icon_color()
        shape = self.icon_shape()
        size = self.icon_size()

        return f"""
            MinimapIcon {size} {color} {shape}
        """

    def icon_color(self) -> categories.COLOR:
        """Customize the look of the map icon that appears in-game"""
        return categories.rarity_to_color(self.rarity)

    def icon_shape(self) -> categories.SHAPE:
        """Customize the look of the map icon that appears in-game"""
        return categories.SHAPE.CIRCLE

    def icon_size(self) -> categories.SIZE:
        """Customize the look of the map icon that appears in-game"""
        return categories.rarity_to_size(self.rarity)

    def beam(self) -> str:
        """Customize the look of the beam of light that appears in-game"""
        color = self.beam_color()
        return f"""
            PlayEffect {color}
        """

    def beam_color(self) -> categories.COLOR:
        """Customize the look of the beam of light that appears in-game"""
        return categories.rarity_to_color(self.rarity)

    def sound(self) -> str:
        """Customize the look of the sound that plays when the item drops in-game"""
        sound = self.sound_file
        return f"""
            DisableDropSound
            CustomAlertSound "{sound}"
        """

    def sound_file(self) -> categories.SOUND:
        """Customize the look of the sound that plays when the item drops in-game"""
        return categories.SOUND.LILY_WOMP

    def __str__(self) -> str:
        """Combine all the rules into a text block"""
        if self.hidden():
            item_rule = f"""
                Hide
                    {self.filter()}
            """
        else:
            item_rule = f"""
                Show
                    {self.filter()}
                    {self.label()}
                    {self.icon()}
                    {self.beam()}
                    {self.sound()}
            """
        return self.format(item_rule)
