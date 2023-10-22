"""A collection of all the categorical values used throughout the code"""

import sys

from enum import Enum, IntEnum


class COLOR(Enum):
    """
    Colors supported by MinimapIcon and PlayEffect
    https://www.pathofexile.com/item-filter/about#:~:text=MinimapIcon
    """

    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    BROWN = "Brown"
    WHITE = "White"
    YELLOW = "Yellow"
    CYAN = "Cyan"
    GREY = "Grey"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"


class SHAPE(Enum):
    """
    Shapes supported by MinimapIcon
    https://www.pathofexile.com/item-filter/about#:~:text=MinimapIcon
    """

    CIRCLE = "Circle"
    DIAMOND = "Diamond"
    HEXAGON = "Hexagon"
    SQUARE = "Square"
    STAR = "Star"
    TRIANGLE = "Triangle"
    CROSS = "Cross"
    MOON = "Moon"
    RAINDROP = "Raindrop"
    KITE = "Kite"
    PENTAGON = "Pentagon"
    UPSIDE_DOWN_HOUSE = "UpsideDownHouse"


class SIZE(Enum):
    """
    Sizes supported by MinimapIcon
    https://www.pathofexile.com/item-filter/about#:~:text=MinimapIcon
    """

    LARGE = "0"
    MEDIUM = "1"
    SMALL = "2"


class RARITY(Enum):
    """Based on the World of Warcraft rarity system."""

    COMMON = "common"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class STRICTNESS(IntEnum):
    """
    Determines how many items are shown.
    Higher strictness means less items are shown.
    """

    LESS_STRICT = 0
    STRICT = 1
    MORE_STRICT = 2
    MAX = sys.maxsize


class SOUND_FILE(Enum):
    """
    Sound files available to play as CustomAlertSound.
    https://www.pathofexile.com/item-filter/about#:~:text=CustomAlertSound
    """

    LILY_AAH = "filter-sounds/lily-aah.mp3"
    LILY_BAM = "filter-sounds/lily-bam.mp3"
    LILY_BING = "filter-sounds/lily-bing-bing.mp3"
    LILY_OOH = "filter-sounds/lily-ooh.mp3"
    LILY_PEKABO = "filter-sounds/lily-pekabo.mp3"
    LILY_SNIFF = "filter-sounds/lily-sniff.mp3"
    LILY_WOMP = "filter-sounds/lily-womp-womp.mp3"
    DISABLED = "None"


class RGB_COLOR(Enum):
    """
    Complete color palette for labels.
    Define font size, text color, background color and border color
    https://www.pathofexile.com/item-filter/about#:~:text=SetBackgroundColor
    """

    BLACK = "0 0 0"
    WHITE = "255 255 255"
    RED = "255 0 0"
    GREEN = "0 255 0"
    BLUE = "0 0 255"
    YELLOW = "255 255 0"
    ORANGE = "255 100 0"
    PINK = "255 0 255"
    PURPLE = "200 0 255"


class FONT_SIZE(Enum):
    """
    Complete color palette for labels.
    Define font size, text color, background color and border color
    https://www.pathofexile.com/item-filter/about#:~:text=SetBackgroundColor
    """

    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


def make_label(
    *,
    font_size: FONT_SIZE = FONT_SIZE.LARGE,
    text_color: RGB_COLOR,
    background_color: RGB_COLOR,
    border_color: RGB_COLOR,
) -> str:
    return f"""
        SetFontSize {font_size.value}
        SetTextColor {text_color.value}
        SetBackgroundColor {background_color.value}
        SetBorderColor {border_color.value}
    """


class LABEL(Enum):
    """
    Complete color palette for labels.
    Define font size, text color, background color and border color
    https://www.pathofexile.com/item-filter/about#:~:text=SetBackgroundColor
    """

    BLACK_ON_WHITE = make_label(
        text_color=RGB_COLOR.BLACK,
        background_color=RGB_COLOR.WHITE,
        border_color=RGB_COLOR.WHITE,
    )
    WHITE_ON_BLACK = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.BLACK,
        border_color=RGB_COLOR.BLACK,
    )
    WHITE_ON_RED = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.RED,
        border_color=RGB_COLOR.RED,
    )
    WHITE_ON_BLUE = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.BLUE,
        border_color=RGB_COLOR.BLUE,
    )
    WHITE_ON_GREEN = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.GREEN,
        border_color=RGB_COLOR.GREEN,
    )
    WHITE_ON_YELLOW = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.YELLOW,
        border_color=RGB_COLOR.YELLOW,
    )
    WHITE_ON_PINK = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.PINK,
        border_color=RGB_COLOR.PINK,
    )
    WHITE_ON_PURPLE = make_label(
        text_color=RGB_COLOR.WHITE,
        background_color=RGB_COLOR.PURPLE,
        border_color=RGB_COLOR.PURPLE,
    )
    ORANGE_ON_BLACK_WITH_BORDER = make_label(
        text_color=RGB_COLOR.ORANGE,
        background_color=RGB_COLOR.BLACK,
        border_color=RGB_COLOR.ORANGE,
    )


def rarity_to_color(rarity: RARITY) -> COLOR:
    """
    Translate rarity to color.
    Based on the World of Warcraft color scheme.
    """
    if rarity == RARITY.COMMON:
        return COLOR.WHITE
    if rarity == RARITY.RARE:
        return COLOR.BLUE
    if rarity == RARITY.EPIC:
        return COLOR.PURPLE
    if rarity == RARITY.LEGENDARY:
        return COLOR.ORANGE

    return COLOR.GREY


def rarity_to_size(rarity: RARITY) -> SIZE:
    """Translate rarity to size."""
    if rarity == RARITY.COMMON:
        return SIZE.SMALL
    if rarity == RARITY.RARE:
        return SIZE.MEDIUM
    if rarity == RARITY.EPIC:
        return SIZE.LARGE
    if rarity == RARITY.LEGENDARY:
        return SIZE.LARGE

    return SIZE.MEDIUM
