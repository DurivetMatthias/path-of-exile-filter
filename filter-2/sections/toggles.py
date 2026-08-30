from enum import StrEnum


class AMULET_TOGGLES(StrEnum):
    ANY = "Any"
    MELEE_LEVEL = "Melee Level"
    MELEE_LEVEL_AND_RES = "Melee level and resistances"


active_amulet_rules = [
    # AMULET.ANY,
    # AMULET.MELEE_LEVEL,
    AMULET_TOGGLES.MELEE_LEVEL_AND_RES,
]


class BELT_TOGGLES(StrEnum):
    ANY = "Any"
    FINE = "Fine"
    FINE_RES = "Fine Resistance"
    UNIQUE = "Unique"


active_belt_rules = [
    # BELT.ANY,
    # BELT.FINE,
    BELT_TOGGLES.FINE_RES,
    BELT_TOGGLES.UNIQUE,
]


class BODY_TOGGLES(StrEnum):
    ANY = "Any"
    SOLDIER = "Soldier Cuirass"
    SOLDIER_RES = "Soldier with Resistance"
    BRASS_DOME = "Brass Dome"


active_body_rules = [
    # BODY.ANY,
    # BODY.SOLDIER,
    # BODY.SOLDIER_RES,
    BODY_TOGGLES.BRASS_DOME,
]


class BOOTS_TOGGLES(StrEnum):
    ANY = "Any"
    TASALIAN = "Tasalian"
    FRACTURE = "Tasalian for fracturing"


active_boots_rules = [
    # BOOTS.ANY,
    # BOOTS.TASALIAN,
    # BOOTS.FRACTURE,
]


class CURRENCY_TOGGLES(StrEnum):
    ARTIFICER = "Artificer's Orb"
    ARMOURER = "Armourer's Scrap"
    GEMCUTTER = "Gemcutter's Prism"
    GLASSBLOWER = "Glassblower's Bauble"
    LESSER_JEWELLER = "Lesser Jeweller's Orb"
    GREATER_JEWELLER = "Greater Jeweller's Orb"


active_currency_rules = [
    # CURRENCY.ARTIFICER,
    # CURRENCY.ARMOURER,
    # CURRENCY.GEMCUTTER,
    # CURRENCY.GLASSBLOWER,
    # CURRENCY.LESSER_JEWELLER,
    # CURRENCY.GREATER_JEWELLER,
]


class SHIELD_TOGGLES(StrEnum):
    ANY = "Any"
    TAWHOAN = "Tawhoan Tower Shield"
    TAWHOAN_RES = "Tawhoan with res"


active_shield_rules = [
    # SHIELD.ANY,
    # SHIELD.TAWHOAN,
    # SHIELD.TAWHOAN_RES,
]


class FLASK_TOGGLES(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good base"
    GOOD_ILVL = "Good item level"
    UNIQUE = "Unique"


active_flask_rules = [
    # FLASK.ANY,
    # FLASK.GOOD_BASE,
    FLASK_TOGGLES.GOOD_ILVL,
    FLASK_TOGGLES.UNIQUE,
]


class RING_TOGGLES(StrEnum):
    ANY = "Any"
    GOOD_BASE = "Good bases"
    RES = "Resistances"


active_ring_rules = [
    # RING.ANY,
    # RING.GOOD_BASE,
    RING_TOGGLES.RES,
]


class OTHER_TOGGLES(StrEnum):
    SEKHEMA = "trial of sekhema key"
    CHAOS = "trial of chaos key"
    BASIC_AUGMENT = "basic augment"


active_other_rules = [
    # OTHER.SEKHEMA,
    # OTHER.CHAOS,
    # OTHER.BASIC_AUGMENT,
]


class MACE_TOGGLES(StrEnum):
    ANY = "Any"
    DAZE = "Fortified or Structured"
    DAZE_4 = "Fortified or Structured and +4"


active_mace_rules = [
    # MACE.ANY,
    # MACE.DAZE,
    # MACE.DAZE_4,
]


class HELMET_TOGGLES(StrEnum):
    ANY = "Any"
    IMPERIAL = "Imperial"
    IMPERIAL_RES = "Imperial with Resistance"
    CONSTRICTING_COMMAND = "Constricting Command"


active_helmet_rules = [
    # HELMET.ANY,
    # HELMET.IMPERIAL,
    # HELMET.IMPERIAL_RES,
    HELMET_TOGGLES.CONSTRICTING_COMMAND,
]


class GLOVES_TOGGLES(StrEnum):
    ANY = "Any"
    MASSIVE = "Massive Mitts"
    MASSIVE_RES = "Massive Mitts with res"


active_gloves_rules = [
    # GLOVES.ANY,
    # GLOVES.MASSIVE,
    # GLOVES.MASSIVE_RES,
]


class GEM_TOGGLES(StrEnum):
    ANY = "Any"
    SUPPORT = "Uncut support lvl 5"
    _18 = "18"
    _19 = "19"
    _20 = "20"


active_gem_rules = [
    # GEM.ANY,
    # GEM.SUPPORT,
    # GEM._18,
    # GEM._19,
    GEM_TOGGLES._20,
]
