from rule import Rule
import rarity_options


class Currency(Rule):
    def label(self) -> str:
        return """
            SetFontSize 45
            SetTextColor 0 0 0
            SetBackgroundColor 255 255 255
            SetBorderColor 255 255 255
        """

    def sound(self) -> str:
        if self.rarity == rarity_options.COMMON:
            return """
                DisableDropSound
            """
        if self.rarity == rarity_options.RARE:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-bing-bing.mp3"
            """
        if self.rarity == rarity_options.EPIC:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-bam.mp3"
            """
        if self.rarity == rarity_options.LEGENDARY:
            return """
                DisableDropSound
                CustomAlertSound "filter-sounds/lily-ooh.mp3"
            """
        return "None"


shard = [
    Currency(
        name="Scroll Fragment",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Binding Shard",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Engineer's Shard",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Horizon Shard",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Transmutation Shard",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Alchemy Shard",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Alteration Shard",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Ancient Shard",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Chaos Shard",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Regal Shard",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Harbinger's Shard",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Annulment Shard",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Exalted Shard",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Fracturing Shard",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Mirror Shard",
        rarity=rarity_options.LEGENDARY,
    ),
]


scroll = [
    Currency(
        name="Portal Scroll",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Scroll of Wisdom",
        rarity=rarity_options.COMMON,
    ),
]

basic = [
    Currency(
        name="Orb of Transmutation",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Orb of Augmentation",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Orb of Chance",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Orb of Alchemy",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Orb of Alteration",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Chaos Orb",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Regal Orb",
        rarity=rarity_options.EPIC,
    ),
]

niche = [
    Currency(
        name="Orb of Binding",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Enkindling Orb",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Instilling Orb",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Orb of Horizons",
        rarity=rarity_options.COMMON,
    ),
]

quality = [
    Currency(
        name="Blacksmith's Whetstone",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Armourer's Scrap",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Engineer's Orb",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Glassblower's Bauble",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Gemcutter's Prism",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Cartographer's Chisel",
        rarity=rarity_options.COMMON,
    ),
]

socket = [
    Currency(
        name="Jeweller's Orb",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Orb of Fusing",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Chromatic Orb",
        rarity=rarity_options.COMMON,
    ),
]

undo = [
    Currency(
        name="Orb of Scouring",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Orb of Regret",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Orb of Unmaking",
        rarity=rarity_options.EPIC,
    ),
]

other = [
    Currency(
        name="Ancient Orb",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Harbinger's Orb",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Vaal Orb",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Blessed Orb",
        rarity=rarity_options.RARE,
    ),
]

sextant = [
    Currency(
        name="Surveyor's Compass",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Awakened Sextant",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Elevated Sextant",
        rarity=rarity_options.EPIC,
    ),
]

legendary = [
    Currency(
        name="Veiled Chaos Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Orb of Annulment",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Divine Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Mirror of Kalandra",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Sacred Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Fracturing Orb",
        rarity=rarity_options.LEGENDARY,
    ),
]

eldritch = [
    Currency(
        name="Lesser Eldritch Ichor",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Greater Eldritch Ichor",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Grand Eldritch Ichor",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Exceptional Eldritch Ichor",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Lesser Eldritch Ember",
        rarity=rarity_options.COMMON,
    ),
    Currency(
        name="Greater Eldritch Ember",
        rarity=rarity_options.RARE,
    ),
    Currency(
        name="Grand Eldritch Ember",
        rarity=rarity_options.EPIC,
    ),
    Currency(
        name="Exceptional Eldritch Ember",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Eldritch Chaos Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Eldritch Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Eldritch Orb of Annulment",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Orb of Conflict",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Orb of Dominance",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Awakener's Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Crusader's Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Hunter's Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Redeemer's Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Warlord's Exalted Orb",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="Crescent Splinter",
        rarity=rarity_options.LEGENDARY,
    ),
    Currency(
        name="The Maven's Writ",
        rarity=rarity_options.LEGENDARY,
    ),
]

rules = [
    *shard,
    *scroll,
    *basic,
    *niche,
    *quality,
    *socket,
    *undo,
    *other,
    *sextant,
    *eldritch,
    *legendary,
]
