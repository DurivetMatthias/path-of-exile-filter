"""A collection of all the categorical values used throughout the code"""

from enum import Enum


class COLOR(Enum):
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
    LARGE = "0"
    MEDIUM = "1"
    SMALL = "2"


class SOUND_FILE(Enum):
    LILY_AAH = "filter-sounds/lily-aah.mp3"
    LILY_BAM = "filter-sounds/lily-bam.mp3"
    LILY_BING = "filter-sounds/lily-bing-bing.mp3"
    LILY_OOH = "filter-sounds/lily-ooh.mp3"
    LILY_PEKABO = "filter-sounds/lily-pekabo.mp3"
    LILY_SNIFF = "filter-sounds/lily-sniff.mp3"
    LILY_WOMP = "filter-sounds/lily-womp-womp.mp3"
    DISABLED = "None"


class BASIC_SOUND(Enum):
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


class VOLUME(Enum):
    QUIET = "25"
    MEDIUM = "100"
    LOUD = "200"


class RGB(Enum):
    BLACK = "0 0 0"
    WHITE = "255 255 255"
    RED = "255 0 0"
    GREEN = "0 255 0"
    BLUE = "0 0 255"
    YELLOW = "255 255 0"
    ORANGE = "255 100 0"
    PINK = "255 0 255"
    PURPLE = "200 0 255"
    CYAN = "0 255 255"
    GREY = "150 150 150"


class FONT_SIZE(Enum):
    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


class RARITY(Enum):
    NORMAL = "normal"
    MAGIC = "magic"
    RARE = "rare"
    UNIQUE = "unique"


class TIER(Enum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


class OPERATOR(Enum):
    EQUAL = "="
    NOT_EQUAL = "!="
    LTE = "<="
    LT = "<"
    GTE = ">="
    GT = ">"
    EXACT = "=="


# TODO list individually
# TODO one hand vs two hand
# TODO other gear classes
class WEAPONS(Enum):
    pass
