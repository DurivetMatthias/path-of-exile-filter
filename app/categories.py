"""A collection of all the categorical values used throughout the code"""

from enum import StrEnum


class COLOR(StrEnum):
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


class SHAPE(StrEnum):
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


class SIZE(StrEnum):
    LARGE = "0"
    MEDIUM = "1"
    SMALL = "2"


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


class RGB(StrEnum):
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


class FONT_SIZE(StrEnum):
    SMALL = "15"
    MEDIUM = "30"
    LARGE = "45"


class RARITY(StrEnum):
    NORMAL = "normal"
    MAGIC = "magic"
    RARE = "rare"
    UNIQUE = "unique"


class TIER(StrEnum):
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


class OPERATOR(StrEnum):
    EQUAL = "="
    NOT_EQUAL = "!="
    LTE = "<="
    LT = "<"
    GTE = ">="
    GT = ">"
    EXACT = "=="


class WEAPON(StrEnum):
    BOW = "Bows"
    CLAW = "Claws"
    DAGGER = "Daggers"
    FISHING_ROD = "Fishing Rods"
    ONE_HAND_AXE = "One Hand Axes"
    ONE_HAND_MACE = "One Hand Maces"
    ONE_HAND_SWORD = "One Hand Swords"
    SCEPTRE = "Sceptres"
    STAFF = "Staves"
    TWO_HAND_AXE = "Two Hand Axes"
    TWO_HAND_MACE = "Two Hand Maces"
    TWO_HAND_SWORD = "Two Hand Swords"
    WAND = "Wands"


class OFFHAND(StrEnum):
    QUIVER = "Quivers"
    SHIELD = "Shields"


class JEWELRY(StrEnum):
    AMULET = "Amulets"
    BELT = "Belts"
    RING = "Rings"


class GEAR(StrEnum):
    BODY_ARMOUR = "Body Armours"
    BOOTS = "Boots"
    GLOVES = "Gloves"
    HELMET = "Helmets"


class FLASK(StrEnum):
    LIFE = "Life Flask"
    MANA = "Mana Flask"
    HYBRID = "Hybrid Flask"
    UTILITY = "Utility Flask"


class AMULET(StrEnum):
    CORAL = "Coral Amulet"
    PAUA = "Paua Amulet"
    AMBER = "Amber Amulet"
    JADE = "Jade Amulet"
    LAPIS = "Lapis Amulet"
    GOLD = "Gold Amulet"
    AGATE = "Agate Amulet"
    CITRINE = "Citrine Amulet"
    TURQUOISE = "Turquoise Amulet"
    ONYX = "Onyx Amulet"


class BELT(StrEnum):
    CHAIN = "Chain Belt"
    RUSTIC = "Rustic Sash"
    STYGIAN = "Stygian Vise"
    HEAVY = "Heavy Belt"
    LEATHER = "Leather Belt"
    CLOTH = "Cloth Belt"
    STUDDED = "Studded Belt"


class RING(StrEnum):
    CORAL = "Coral Ring"
    IRON = "Iron Ring"
    PAUA = "Paua Ring"
    UNSET = "Unset Ring"
    SAPPHIRE = "Sapphire Ring"
    TOPAZ = "Topaz Ring"
    RUBY = "Ruby Ring"
    DIAMOND = "Diamond Ring"
    GOLD = "Gold Ring"
    MOONSTONE = "Moonstone Ring"
    TWO_STONE = "Two-Stone Ring"
    BONE = "Bone Ring"
    AMETHYST = "Amethyst Ring"
    PRISMATIC = "Prismatic Ring"
    VERMILLION = "Vermillion Ring"


class JEWEL(StrEnum):
    COBALT = "Cobalt Jewel"
    CRIMSON = "Crimson Jewel"
    VIRIDIAN = "Viridian Jewel"
    SMALL_CLUSTER = "Small Cluster Jewel"
    MEDIUM_CLUSTER = "Medium Cluster Jewel"
    LARGE_CLUSTER = "Large Cluster Jewel"
    GHASTLY = "Ghastly Eye Jewel"
    HYPNOTIC = "Hypnotic Eye Jewel"
    MURDEROUS = "Murderous Eye Jewel"
    SEARCHING = "Searching Eye Jewel"


class CURRENCY(StrEnum):
    ORB_OF_TRANSMUTATION = "Orb of Transmutation"
    ORB_OF_AUGMENTATION = "Orb of Augmentation"
    ORB_OF_ALTERATION = "Orb of Alteration"
    ORB_OF_FUSING = "Orb of Fusing"
    ORB_OF_ALCHEMY = "Orb of Alchemy"
    CHAOS_ORB = "Chaos Orb"
    GEMCUTTERS_PRISM = "Gemcutters Prism"
    EXALTED_ORB = "Exalted Orb"
    CHROMATIC_ORB = "Chromatic Orb"
    JEWELLERS_ORB = "Jeweller's Orb"
    ENGINEERS_ORB = "Engineer's Orb"
    ORB_OF_CHANCE = "Orb of Chance"
    ORB_OF_SCOURING = "Orb of Scouring"
    BLESSED_ORB = "Blessed Orb"
    ORB_OF_REGRET = "Orb of Regret"
    REGAL_ORB = "Regal Orb"
    DIVINE_ORB = "Divine Orb"
    VAAL_ORB = "Vaal Orb"
    ORB_OF_ANNULMENT = "Orb of Annulment"
    ORB_OF_BINDING = "Orb of Binding"
    ANCIENT_ORB = "Ancient Orb"
    ORB_OF_HORIZONS = "Orb of Horizons"
    HARBINGERS_ORB = "Harbinger's Orb"
    FRACTURING_ORB = "Fracturing Orb"
    ARMOURERS_SCRAP = "Armourer's Scrap"
    BLACKSMITHS_WHETSTONE = "Blacksmith's Whetstone"
    GLASSBLOWERS_BAUBLE = "Glassblower's Bauble"
    MIRROR_OF_KALANDRA = "Mirror of Kalandra"
    ORB_OF_UNMAKING = "Orb of Unmaking"
    VEILED_ORB = "Veiled Orb"
    ENKINDLING_ORB = "Enkindling Orb"
    INSTILLING_ORB = "Instilling Orb"
    SACRED_ORB = "Sacred Orb"


class HARVEST(StrEnum):
    WILD = "Wild Crystallised Lifeforce"
    VIVID = "Vivid Crystallised Lifeforce"
    PRIMAL = "Primal Crystallised Lifeforce"
    SACRED = "Sacred Crystallised Lifeforce"


class BREACH_SPLINTER(StrEnum):
    XOPH = "Splinter of Xoph"
    TUL = "Splinter of Tul"
    ESH = "Splinter of Esh"
    UUL = "Splinter of Uul-Netol"
    CHAYULA = "Splinter of Chayula"


class BREACHSTONE(StrEnum):
    XOPH = "Breachstone of Xoph"
    TUL = "Breachstone of Tul"
    ESH = "Breachstone of Esh"
    UUL = "Breachstone of Uul-Netol"
    CHAYULA = "Breachstone of Chayula"


class BREACH_BLESSING(StrEnum):
    XOPH = "Blessing of Xoph"
    TUL = "Blessing of Tul"
    ESH = "Blessing of Esh"
    UUL = "Blessing of Uul-Netol"
    CHAYULA = "Blessing of Chayula"


class BEYOND_CURRENCY(StrEnum):
    ARMOURERS_SCRAP = "Tainted Armourer's Scrap"
    BLACKSMITHS_WHETSTONE = "Tainted Blacksmith's Whetstone"
    CHROMATIC_ORB = "Tainted Chromatic Orb"
    JEWELELRS_ORB = "Tainted Jeweller's Orb"
    FUSING = "Tainted Orb of Fusing"
    MYTHIC_ORB = "Tainted Mythic Orb"
    CHAOS_ORB = "Tainted Chaos Orb"
    EXALTED = "Tainted Exalted Orb"
    DIVINE = "Tainted Divine Teardrop"
