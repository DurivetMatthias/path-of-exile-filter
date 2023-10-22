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
        strictness: int = categories.STRICTNESS.MAX,
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

    def filter(self) -> str:
        """Limit the rule to certain properties of the item"""
        return f'BaseType == "{self.name}"'

    def hidden(self) -> bool:
        """Determines if this becomes a Hide or Show rule"""
        return self.hide

    def label(self) -> categories.LABEL:
        """Customize the look of the label that appears in-game"""
        return categories.LABEL.WHITE_ON_BLACK

    def icon(self) -> str:
        """Customize the look of the map icon that appears in-game"""
        color = self.icon_color().value
        shape = self.icon_shape().value
        size = self.icon_size().value

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
        color = self.beam_color().value
        return f"""
            PlayEffect {color}
        """

    def beam_color(self) -> categories.COLOR:
        """Customize the look of the beam of light that appears in-game"""
        return categories.rarity_to_color(self.rarity)

    def sound(self) -> str:
        """Customize the look of the sound that plays when the item drops in-game"""
        sound_file = self.sound_file().value
        return f"""
            DisableDropSound
            CustomAlertSound "{sound_file}" 300
        """

    def sound_file(self) -> categories.SOUND_FILE:
        """Customize the look of the sound that plays when the item drops in-game"""
        if self.rarity == categories.RARITY.COMMON:
            return categories.SOUND_FILE.DISABLED
        if self.rarity == categories.RARITY.RARE:
            return categories.SOUND_FILE.LILY_BING
        if self.rarity == categories.RARITY.EPIC:
            return categories.SOUND_FILE.LILY_BAM
        if self.rarity == categories.RARITY.LEGENDARY:
            return categories.SOUND_FILE.LILY_OOH

        return categories.SOUND_FILE.DISABLED

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
                    {self.label().value}
                    {self.icon()}
                    {self.beam()}
                    {self.sound()}
            """
        return self.format(item_rule)
