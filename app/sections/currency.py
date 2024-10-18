from app.base_types import *
from app.blocks import Show
from app.conditions.compound import MultiBaseType, TierStyle
from app.categories import TIER

HIDE = "Hide"
COMMON = "common"
RARE = "rare"
EPIC = "epic"
LEGENDARY = "legendary"

currencies = {
    "Gold": RARE,
    # Currency
    ORB_OF_ALTERATION: EPIC,
    ORB_OF_FUSING: RARE,
    ORB_OF_ALCHEMY: RARE,
    CHAOS_ORB: EPIC,
    GEMCUTTERS_PRISM: RARE,
    EXALTED_ORB: LEGENDARY,
    CHROMATIC_ORB: RARE,
    JEWELLERS_ORB: RARE,
    ENGINEERS_ORB: RARE,
    INFUSED_ENGINEERS_ORB: LEGENDARY,
    ORB_OF_CHANCE: RARE,
    QUANTITY_CHISEL: RARE,
    RARITY_CHISEL: EPIC,
    PACK_CHISEL: EPIC,
    SCARAB_CHISEL: EPIC,
    CURRENCY_CHISEL: EPIC,
    DIVINATION_CHISEL: EPIC,
    ORB_OF_SCOURING: RARE,
    BLESSED_ORB: RARE,
    ORB_OF_REGRET: RARE,
    REGAL_ORB: RARE,
    DIVINE_ORB: LEGENDARY,
    VAAL_ORB: RARE,
    ORB_OF_ANNULMENT: LEGENDARY,
    ORB_OF_BINDING: RARE,
    ANCIENT_ORB: EPIC,
    ORB_OF_HORIZONS: RARE,
    HARBINGERS_ORB: EPIC,
    FRACTURING_ORB: LEGENDARY,
    SCROLL_OF_WISDOM: RARE,
    PORTAL_SCROLL: RARE,
    ARMOURERS_SCRAP: RARE,
    BLACKSMITHS_WHETSTONE: RARE,
    GLASSBLOWERS_BAUBLE: RARE,
    ORB_OF_TRANSMUTATION: RARE,
    ORB_OF_AUGMENTATION: RARE,
    MIRROR_OF_KALANDRA: LEGENDARY,
    TEMPERING_ORB: LEGENDARY,
    TAILORING_ORB: LEGENDARY,
    ORB_OF_UNMAKING: EPIC,
    VEILED_ORB: LEGENDARY,
    ENKINDLING_ORB: RARE,
    INSTILLING_ORB: RARE,
    SACRED_ORB: LEGENDARY,
    STACKED_DECK: RARE,
    # Exotic currency
    CRUSADERS_EXALTED_ORB: LEGENDARY,
    REDEEMERS_EXALTED_ORB: LEGENDARY,
    HUNTERS_EXALTED_ORB: LEGENDARY,
    WARLORDS_EXALTED_ORB: LEGENDARY,
    AWAKENERS_ORB: LEGENDARY,
    ORB_OF_DOMINANCE: LEGENDARY,
    ELDRITCH_CHAOS_ORB: LEGENDARY,
    ELDRITCH_EXALTED_ORB: LEGENDARY,
    ELDRITCH_ORB_OF_ANNULMENT: LEGENDARY,
    LESSER_ELDRITCH_EMBER: RARE,
    GREATER_ELDRITCH_EMBER: RARE,
    GRAND_ELDRITCH_EMBER: LEGENDARY,
    EXCEPTIONAL_ELDRITCH_EMBER: LEGENDARY,
    LESSER_ELDRITCH_ICHOR: RARE,
    GREATER_ELDRITCH_ICHOR: RARE,
    GRAND_ELDRITCH_ICHOR: LEGENDARY,
    EXCEPTIONAL_ELDRITCH_ICHOR: LEGENDARY,
    ORB_OF_CONFLICT: LEGENDARY,
    TAINTED_CHROMATIC_ORB: LEGENDARY,
    TAINTED_ORB_OF_FUSING: LEGENDARY,
    TAINTED_JEWELLERS_ORB: LEGENDARY,
    TAINTED_CHAOS_ORB: LEGENDARY,
    TAINTED_EXALTED_ORB: LEGENDARY,
    TAINTED_MYTHIC_ORB: LEGENDARY,
    TAINTED_ARMOURERS_SCRAP: LEGENDARY,
    TAINTED_BLACKSMITHS_WHETSTONE: LEGENDARY,
    TAINTED_DIVINE_TEARDROP: LEGENDARY,
    WILD_CRYSTALLISED_LIFEFORCE: EPIC,
    VIVID_CRYSTALLISED_LIFEFORCE: EPIC,
    PRIMAL_CRYSTALLISED_LIFEFORCE: EPIC,
    SACRED_CRYSTALLISED_LIFEFORCE: EPIC,
    HINEKORAS_LOCK: LEGENDARY,
    # Shards & Splinters
    TRANSMUTATION_SHARD: RARE,
    ALTERATION_SHARD: RARE,
    ALCHEMY_SHARD: RARE,
    CHAOS_SHARD: EPIC,
    EXALTED_SHARD: LEGENDARY,
    ENGINEERS_SHARD: RARE,
    REGAL_SHARD: RARE,
    ANNULMENT_SHARD: LEGENDARY,
    BINDING_SHARD: RARE,
    ANCIENT_SHARD: RARE,
    HORIZON_SHARD: RARE,
    HARBINGERS_SHARD: RARE,
    FRACTURING_SHARD: LEGENDARY,
    MIRROR_SHARD: LEGENDARY,
    SPLINTER_OF_XOPH: COMMON,
    SPLINTER_OF_TUL: COMMON,
    SPLINTER_OF_ESH: COMMON,
    SPLINTER_OF_UUL_NETOL: COMMON,
    SPLINTER_OF_CHAYULA: EPIC,
    TIMELESS_ETERNAL_EMPIRE_SPLINTER: EPIC,
    TIMELESS_KARUI_SPLINTER: EPIC,
    TIMELESS_VAAL_SPLINTER: EPIC,
    TIMELESS_TEMPLAR_SPLINTER: EPIC,
    TIMELESS_MARAKETH_SPLINTER: EPIC,
    SIMULACRUM_SPLINTER: EPIC,
    CRESCENT_SPLINTER: EPIC,
    RITUAL_SPLINTER: EPIC,
    # fragments
    SACRIFICE_AT_DUSK: COMMON,
    SACRIFICE_AT_MIDNIGHT: COMMON,
    SACRIFICE_AT_DAWN: COMMON,
    SACRIFICE_AT_NOON: COMMON,
    MORTAL_GRIEF: RARE,
    MORTAL_RAGE: RARE,
    MORTAL_HOPE: RARE,
    MORTAL_IGNORANCE: RARE,
    FRAGMENT_OF_THE_HYDRA: LEGENDARY,
    FRAGMENT_OF_THE_PHOENIX: LEGENDARY,
    FRAGMENT_OF_THE_MINOTAUR: LEGENDARY,
    FRAGMENT_OF_THE_CHIMERA: LEGENDARY,
    FRAGMENT_OF_ENSLAVEMENT: LEGENDARY,
    FRAGMENT_OF_ERADICATION: LEGENDARY,
    FRAGMENT_OF_CONSTRICTION: LEGENDARY,
    FRAGMENT_OF_PURIFICATION: LEGENDARY,
    FRAGMENT_OF_TERROR: LEGENDARY,
    FRAGMENT_OF_EMPTINESS: LEGENDARY,
    FRAGMENT_OF_SHAPE: LEGENDARY,
    FRAGMENT_OF_KNOWLEDGE: LEGENDARY,
    AL_HEZMINS_CREST: LEGENDARY,
    BARANS_CREST: LEGENDARY,
    DROXS_CREST: LEGENDARY,
    VERITANIAS_CREST: LEGENDARY,
    # BEAUTY:LEGENDARY,
    # CURIOSITY:LEGENDARY,
    # AMBITION:LEGENDARY,
    # COOPERATION:LEGENDARY,
    OFFERING_TO_THE_GODDESS: COMMON,
    TRIBUTE_TO_THE_GODDESS: LEGENDARY,
    GIFT_TO_THE_GODDESS: LEGENDARY,
    DEDICATION_TO_THE_GODDESS: LEGENDARY,
    XOPHS_BREACHSTONE: LEGENDARY,
    TULS_BREACHSTONE: LEGENDARY,
    ESHS_BREACHSTONE: LEGENDARY,
    UUL_NETOLS_BREACHSTONE: LEGENDARY,
    CHAYULAS_BREACHSTONE: LEGENDARY,
    XOPHS_FLAWLESS_BREACHSTONE: LEGENDARY,
    TULS_FLAWLESS_BREACHSTONE: LEGENDARY,
    ESHS_FLAWLESS_BREACHSTONE: LEGENDARY,
    UUL_NETOLS_FLAWLESS_BREACHSTONE: LEGENDARY,
    CHAYULAS_FLAWLESS_BREACHSTONE: LEGENDARY,
    BLESSING_OF_XOPH: LEGENDARY,
    BLESSING_OF_TUL: LEGENDARY,
    BLESSING_OF_ESH: LEGENDARY,
    BLESSING_OF_UUL_NETOL: LEGENDARY,
    BLESSING_OF_CHAYULA: LEGENDARY,
    TIMELESS_ETERNAL_EMBLEM: LEGENDARY,
    TIMELESS_KARUI_EMBLEM: LEGENDARY,
    TIMELESS_VAAL_EMBLEM: LEGENDARY,
    TIMELESS_TEMPLAR_EMBLEM: LEGENDARY,
    TIMELESS_MARAKETH_EMBLEM: LEGENDARY,
    SIMULACRUM: LEGENDARY,
    SACRED_BLOSSOM: LEGENDARY,
    RITUAL_VESSEL: LEGENDARY,
    "Blood-filled Vessel": EPIC,
    THE_MAVENS_WRIT: LEGENDARY,
    WRITHING_INVITATION: LEGENDARY,
    SCREAMING_INVITATION: LEGENDARY,
    POLARIC_INVITATION: LEGENDARY,
    INCANDESCENT_INVITATION: LEGENDARY,
    ANCIENT_RELIQUARY_KEY: LEGENDARY,
    TIMEWORN_RELIQUARY_KEY: LEGENDARY,
    VAAL_RELIQUARY_KEY: LEGENDARY,
    FORGOTTEN_RELIQUARY_KEY: LEGENDARY,
    VISCERAL_RELIQUARY_KEY: LEGENDARY,
    SHINY_RELIQUARY_KEY: LEGENDARY,
    ARCHIVE_RELIQUARY_KEY: LEGENDARY,
    OUBLIETTE_RELIQUARY_KEY: LEGENDARY,
    COSMIC_RELIQUARY_KEY: LEGENDARY,
    DECAYING_RELIQUARY_KEY: LEGENDARY,
    VOIDBORN_RELIQUARY_KEY: LEGENDARY,
    VALDOS_PUZZLE_BOX: LEGENDARY,
    DIVINE_VESSEL: RARE,
    # omens
    OMEN_OF_AMELIORATION: EPIC,
    # OMEN_OF_RETURN:EPIC,
    OMEN_OF_DEATH_DANCING: EPIC,
    # OMEN_OF_REFRESHMENT:EPIC,
    # OMEN_OF_THE_SOUL_DEVOURER:EPIC,
    OMEN_OF_FORTUNE: EPIC,
    OMEN_OF_THE_JEWELLER: EPIC,
    OMEN_OF_CONNECTIONS: EPIC,
    OMEN_OF_BLANCHING: EPIC,
    # OMEN_OF_ADRENALINE:EPIC,
    OMEN_OF_DEATHS_DOOR: EPIC,
    # OMEN_OF_BRILLIANCE:EPIC,
    # Sanctum
    FORBIDDEN_TOME: EPIC,
    # Scouting Report
    EXPLORERS_SCOUTING_REPORT: RARE,
    VAAL_SCOUTING_REPORT: RARE,
    SINGULAR_SCOUTING_REPORT: RARE,
    INFLUENCED_SCOUTING_REPORT: EPIC,
    COMPREHENSIVE_SCOUTING_REPORT: EPIC,
    OTHERWORLDLY_SCOUTING_REPORT: EPIC,
    DELIRIOUS_SCOUTING_REPORT: EPIC,
    OPERATIVES_SCOUTING_REPORT: EPIC,
    BLIGHTED_SCOUTING_REPORT: EPIC,
    # Expedition
    ASTRAGALI: EPIC,
    EXOTIC_COINAGE: EPIC,
    SCRAP_METAL: EPIC,
    BURIAL_MEDALLION: EPIC,
    "Expedition Logbook": LEGENDARY,
    # Delirium Orbs
    FINE_DELIRIUM_ORB: EPIC,
    SINGULAR_DELIRIUM_ORB: EPIC,
    THAUMATURGES_DELIRIUM_ORB: EPIC,
    BLACKSMITHS_DELIRIUM_ORB: EPIC,
    ARMOURSMITHS_DELIRIUM_ORB: EPIC,
    CARTOGRAPHERS_DELIRIUM_ORB: EPIC,
    JEWELLERS_DELIRIUM_ORB: EPIC,
    ABYSSAL_DELIRIUM_ORB: EPIC,
    KALGUURAN_DELIRIUM_ORB: EPIC,
    FOREBODING_DELIRIUM_ORB: EPIC,
    OBSCURED_DELIRIUM_ORB: EPIC,
    WHISPERING_DELIRIUM_ORB: EPIC,
    FRAGMENTED_DELIRIUM_ORB: EPIC,
    SKITTERING_DELIRIUM_ORB: EPIC,
    FOSSILISED_DELIRIUM_ORB: EPIC,
    DIVINERS_DELIRIUM_ORB: EPIC,
    DELIRIUM_ORB: EPIC,
    PRIMAL_DELIRIUM_ORB: EPIC,
    TIMELESS_DELIRIUM_ORB: EPIC,
    BLIGHTED_DELIRIUM_ORB: EPIC,
    CHALLENGING_DELIRIUM_ORB: EPIC,
    # Catalyst
    TURBULENT_CATALYST: EPIC,
    IMBUED_CATALYST: EPIC,
    ABRASIVE_CATALYST: EPIC,
    TEMPERING_CATALYST: EPIC,
    FERTILE_CATALYST: EPIC,
    PRISMATIC_CATALYST: EPIC,
    INTRINSIC_CATALYST: EPIC,
    NOXIOUS_CATALYST: EPIC,
    ACCELERATING_CATALYST: EPIC,
    UNSTABLE_CATALYST: EPIC,
    TAINTED_CATALYST: EPIC,
    # Oil
    CLEAR_OIL: EPIC,
    SEPIA_OIL: EPIC,
    AMBER_OIL: EPIC,
    VERDANT_OIL: EPIC,
    TEAL_OIL: EPIC,
    AZURE_OIL: EPIC,
    INDIGO_OIL: EPIC,
    VIOLET_OIL: EPIC,
    CRIMSON_OIL: EPIC,
    BLACK_OIL: EPIC,
    OPALESCENT_OIL: EPIC,
    SILVER_OIL: EPIC,
    GOLDEN_OIL: EPIC,
    TAINTED_OIL: EPIC,
    REFLECTIVE_OIL: EPIC,
    OIL_EXTRACTOR: EPIC,
    # Delve
    PRIMITIVE_CHAOTIC_RESONATOR: EPIC,
    POTENT_CHAOTIC_RESONATOR: EPIC,
    POWERFUL_CHAOTIC_RESONATOR: EPIC,
    PRIME_CHAOTIC_RESONATOR: EPIC,
    SCORCHED_FOSSIL: EPIC,
    FRIGID_FOSSIL: EPIC,
    METALLIC_FOSSIL: EPIC,
    JAGGED_FOSSIL: EPIC,
    ABERRANT_FOSSIL: EPIC,
    PRISTINE_FOSSIL: EPIC,
    DENSE_FOSSIL: EPIC,
    CORRODED_FOSSIL: EPIC,
    PRISMATIC_FOSSIL: EPIC,
    AETHERIC_FOSSIL: EPIC,
    SERRATED_FOSSIL: EPIC,
    LUCENT_FOSSIL: EPIC,
    SHUDDERING_FOSSIL: EPIC,
    BOUND_FOSSIL: EPIC,
    "Opulent Fossil": EPIC,
    DEFT_FOSSIL: EPIC,
    FUNDAMENTAL_FOSSIL: EPIC,
    FACETED_FOSSIL: EPIC,
    BLOODSTAINED_FOSSIL: EPIC,
    HOLLOW_FOSSIL: EPIC,
    FRACTURED_FOSSIL: EPIC,
    GLYPHIC_FOSSIL: EPIC,
    TANGLED_FOSSIL: EPIC,
    SANCTIFIED_FOSSIL: EPIC,
    GILDED_FOSSIL: EPIC,
    # Labyrinth
    "Golden Key": EPIC,
    "Treasure Key": EPIC,
    "Silver Key": RARE,
    # Incursion
    STONE_OF_PASSAGE: LEGENDARY,
    CHRONICLE_OF_ATZOATL: LEGENDARY,
    # Uber fragments
    SYNTHESISING_FRAGMENT: LEGENDARY,
    DEVOURING_FRAGMENT: LEGENDARY,
    BLAZING_FRAGMENT: LEGENDARY,
    REALITY_FRAGMENT: LEGENDARY,
    COSMIC_FRAGMENT: LEGENDARY,
    AWAKENING_FRAGMENT: LEGENDARY,
    DECAYING_FRAGMENT: LEGENDARY,
}


hidden = [name for (name, tier) in currencies.items() if tier == HIDE]
common = [name for (name, tier) in currencies.items() if tier == COMMON]
rare = [name for (name, tier) in currencies.items() if tier == RARE]
epic = [name for (name, tier) in currencies.items() if tier == EPIC]
legendary = [name for (name, tier) in currencies.items() if tier == LEGENDARY]


rules = [
    # Hide(
    #     [
    #         MultiBaseType(hidden),
    #     ],
    # ),
    Show(
        [
            MultiBaseType(common),
            TierStyle(TIER.COMMON),
        ],
    ),
    Show(
        [
            MultiBaseType(rare),
            TierStyle(TIER.RARE),
        ],
    ),
    Show(
        [
            MultiBaseType(epic),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType(legendary),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
