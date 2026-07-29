from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *
from app.rule_map import *


rule_map = {
    # Common
    "Grave Knowledge": RULE.COMMON,
    # Rare
    "Lucky Deck": RULE.RARE,
    "More is Never Enough": RULE.RARE,
    "The Cache": RULE.RARE,
    "The Encroaching Darkness": RULE.RARE,
    "The Sun": RULE.RARE,  # Rise of the Phoenix
    "The Escape": RULE.RARE,
    "The Tinkerer's Table": RULE.RARE,
    "The Tireless Extractor": RULE.RARE,
    "The Professor": RULE.LEGENDARY,  # Multi-mod craft
    "The Twilight Moon": RULE.RARE,
    "The Void": RULE.RARE,
    "The Wolf's Legacy": RULE.RARE,
    "Three Voices": RULE.RARE,
    # Epic
    "A Sea of Blue": RULE.EPIC,
    "Acclimatisation": RULE.EPIC,
    "Abandoned Wealth": RULE.EPIC,
    "Alluring Bounty": RULE.EPIC,
    "Avian Pursuit": RULE.EPIC,
    "Brother's Stash": RULE.EPIC,
    "Cameria's Cut": RULE.EPIC,
    "Chaotic Disposition": RULE.EPIC,
    "Demigod's Wager": RULE.EPIC,
    "Ever-Changing": RULE.EPIC,
    "Guardian's Challenge": RULE.EPIC,
    "Justified Ambition": RULE.EPIC,
    "Lingering Remnants": RULE.EPIC,
    "No Traces": RULE.EPIC,
    "Society's Remorse": RULE.EPIC,
    "The Coming Storm": RULE.EPIC,
    "The Endurance": RULE.EPIC,
    "Shard of Fate": RULE.EPIC,
    "The Finishing Touch": RULE.EPIC,
    "The Innocent": RULE.EPIC,
    "The Price of Protection": RULE.EPIC,
    "The Scout": RULE.EPIC,
    "The Seeker": RULE.EPIC,
    "The Spark and the Flame": RULE.EPIC,
    "The Wilted Rose": RULE.EPIC,
    "The Wrath": RULE.EPIC,
    "The Wretched": RULE.EPIC,
    "Three Faces in the Dark": RULE.EPIC,
    "Vinia's Token": RULE.EPIC,
    "The Hoarder": RULE.EPIC,
    "The Saint's Treasure": RULE.EPIC,
    # Legendary
    "Astral Protection": RULE.LEGENDARY,
    "Brother's Gift": RULE.LEGENDARY,
    "Divine Beauty": RULE.LEGENDARY,
    "History": RULE.LEGENDARY,
    "House of Mirrors": RULE.LEGENDARY,
    "I See Brothers": RULE.LEGENDARY,
    "Lethean Temptation": RULE.LEGENDARY,
    "Lonely Warrior": RULE.LEGENDARY,
    "Love Through Ice": RULE.LEGENDARY,
    "Reflection of the Heart": RULE.LEGENDARY,
    "The Apothecary": RULE.LEGENDARY,
    "The Artist": RULE.LEGENDARY,
    "The Demon": RULE.LEGENDARY,
    "The Doctor": RULE.LEGENDARY,
    "The Dragon's Heart": RULE.LEGENDARY,
    "The Eye of Terror": RULE.LEGENDARY,
    "The Eye of the Dragon": RULE.LEGENDARY,
    "The Fiend": RULE.LEGENDARY,
    "The Fortunate": RULE.LEGENDARY,
    "The Immortal": RULE.LEGENDARY,
    "The Insane Cat": RULE.LEGENDARY,
    "The Journey": RULE.LEGENDARY,
    "The Lake": RULE.LEGENDARY,
    "The Long Con": RULE.LEGENDARY,
    "The Mad King": RULE.LEGENDARY,
    "The Nurse": RULE.LEGENDARY,
    "The Patient": RULE.LEGENDARY,
    "The Polymath": RULE.LEGENDARY,
    "The Price of Devotion": RULE.LEGENDARY,
    "The Sephirot": RULE.LEGENDARY,
    "The Shortcut": RULE.LEGENDARY,
    "The Slumbering Beast": RULE.LEGENDARY,
    "Unrequited Love": RULE.LEGENDARY,
    # New cards
    "Pearls Before Swine": RULE.LEGENDARY,
    "Energy Sword": RULE.LEGENDARY,
    "Divine Shard": RULE.LEGENDARY,
}


rules = [
    *map_to_rules(rule_map),
    Show([BaseType("Stacked Deck"), TierStyle(TIER.COMMON)]),
    Hide([Class("Divination Cards")]),
]
