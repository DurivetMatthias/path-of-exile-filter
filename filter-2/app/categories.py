"""A collection of all the categorical values used throughout the code"""

from enum import StrEnum


class COLOR(StrEnum):
    RED = "Red"
    CYAN = "Cyan"
    GREY = "Grey"
    BLUE = "Blue"
    PINK = "Pink"
    GREEN = "Green"
    BROWN = "Brown"
    WHITE = "White"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    PURPLE = "Purple"


class SHAPE(StrEnum):
    STAR = "Star"
    MOON = "Moon"
    KITE = "Kite"
    CROSS = "Cross"
    CIRCLE = "Circle"
    SQUARE = "Square"
    DIAMOND = "Diamond"
    HEXAGON = "Hexagon"
    TRIANGLE = "Triangle"
    RAINDROP = "Raindrop"
    PENTAGON = "Pentagon"
    UPSIDE_DOWN_HOUSE = "UpsideDownHouse"


class SIZE(StrEnum):
    SMALL = "2"
    MEDIUM = "1"
    LARGE = "0"


class BASIC_SOUND(StrEnum):
    DISABLED = "None"
    CYMBAL = "1"
    GUN = "2"
    BELL = "3"
    ROTATION = "4"
    ELECTRICITY = "5"
    NEEDLE = "6"
    RIPPLE = "7"
    INVERTED_RIPPLE = "8"
    SLOW_RIPPLE = "9"
    TINK = "10"
    PISTOL = "11"
    METRONOME = "12"
    TAMBOURINE = "13"
    SLOW_TREMBLE = "14"
    TREMBLE = "15"
    PUNCH = "16"


class VOLUME(StrEnum):
    QUIET = "25"
    MEDIUM = "100"
    LOUD = "200"
    MAX = "300"


class RGB(StrEnum):
    RED = "255 0 0"
    BLACK = "0 0 0"
    BLUE = "0 0 255"
    GREEN = "0 255 0"
    PINK = "255 0 255"
    CYAN = "0 255 255"
    YELLOW = "255 255 0"
    ORANGE = "255 100 0"
    GREY = "150 150 150"
    PURPLE = "200 0 255"
    WHITE = "255 255 255"


class FONT_SIZE(StrEnum):
    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


class OPERATOR(StrEnum):
    CONTAINS = "="
    NOT_EQUAL = "!="
    LTE = "<="
    LT = "<"
    GTE = ">="
    GT = ">"
    EXACT = "=="


class RARITY(StrEnum):
    NORMAL = "normal"
    MAGIC = "magic"
    RARE = "rare"
    UNIQUE = "unique"


# ==================
# Custom definitions
# ==================


class TIER(StrEnum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"
