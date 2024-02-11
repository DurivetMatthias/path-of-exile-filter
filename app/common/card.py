from app import categories, extensions
from app.rules import Rule

# TODO automate
# Cards with extremely valuable rewards
legendary = [
    "A Dab of Ink",
    "Abandoned Wealth",
    "Alluring Bounty",
    "Brother's Gift",
    "Brother's Stash",
    "Brush, Paint and Palette",
    "Darker Half",
    "Demigod's Wager",
    "Desecrated Virtue",
    "Divine Beauty",
    "Doryani's Epiphany",
    "Eternal Bonds",
    "Ever-Changing",
    "Gemcutter's Mercy",
    "Harmony of Souls",
    "Home",
    "House of Mirrors",
    "Imperfect Memories",
    "Keeper's Corruption",
    "Luminous Trove",
    "Magnum Opus",
    "No Traces",
    "Nook's Crown",
    "Peaceful Moments",
    "Seven Years Bad Luck",
    "The Apothecary",
    "The Artist",
    "The Cheater",
    "The Demon",
    "The Destination",
    "The Doctor",
    "The Dragon's Heart",
    "The Enlightened",
    "The Eternal War",
    "The Eye of the Dragon",
    "The Fiend",
    "The Fishmonger",
    "The Fortunate",
    "The Garish Power",
    "The Hoarder",
    "The Immortal",
    "The Innocent",
    "The Insane Cat",
    "The Leviathan",
    "The Long Con",
    "The Nurse",
    "The Old Man",
    "The Patient",
    "The Price of Devotion",
    "The Rusted Bard",
    "The Saint's Treasure",
    "The Samurai's Eye",
    "The Scout",
    "The Seeker",
    "The Sephirot",
    "The Shortcut",
    "The Transformation",
    "Unrequited Love",
    "Wealth and Power",
    "The Mad King",
    "The Hunger",
]

# Cards with useful results
epic = [
    "A Sea of Blue",
    "Acclimatisation",
    "Ambitious Obsession",
    "Chaotic Disposition",
    "Coveted Possession",
    "Dementophobia",
    "Destined to Crumble",
    "Disdain",
    "Duality",
    "Guardian's Challenge",
    "Judging Voices",
    "Last Hope",
    "Lucky Connections",
    "Lucky Deck",
    "Monochrome",
    "Sambodhi's Vow",
    "More is Never Enough",
    "Rebirth and Renewal",
    "Shard of Fate",
    "Society's Remorse",
    "Something Dark",
    "The Cacophony",
    "The Card Sharp",
    "The Cartographer",
    "The Dapper Prodigy",
    "The Eldritch Decay",
    "The Endurance",
    "The Finishing Touch",
    "The Heroic Shot",
    "The Inventor",
    "The Journey",
    "The Landing",
    "The Master Artisan",
    "The Puzzle",
    "The Side Quest",
    "The Tinkerer's Table",
    "The Tireless Extractor",
    "The Union",
    "The Void",
    "The Wrath",
    "Three Faces in the Dark",
    "Three Voices",
    "Underground Forest",
    "Vinia's Token",
    "The Coming Storm",
    "The One With All",
]

# Rare cards that give an interesting reward
rare = [
    "A Dusty Memory",
    "A Fate Worse Than Death",
    "A Modest Request",
    "A Stone Perfected",
    "Altered Perception",
    "Arrogance of the Vaal",
    "Auspicious Ambitions",
    "Azyran's Reward",
    "Baited Expectations",
    "Bijoux",
    "Cameria's Cut",
    "Chasing Risk",
    "Checkmate",
    "Costly Curio",
    "Deathly Designs",
    "Glimmer of Hope",
    "Grave Knowledge",
    "Humility",
    "Lachrymal Necrosis",
    "Lingering Remnants",
    "Man With Bear",
    "Matryoshka",
    "Scholar of the Seas",
    "The Cache",
    "The Catch",
    "The Chains that Bind",
    "The Deal",
    "The Dreamland",
    "The Easy Stroll",
    "The Encroaching Darkness",
    "The Magma Crab",
    "The Obscured",
    "The Porcupine",
    "The Price of Prescience",
    "The Price of Protection",
    "The Professor",
    "The Risk",
    "The Twilight Moon",
    "Vanity",
    "Time-Lost Relic",
]

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Stacked Deck"),
            extensions.TierStyle(tier=categories.TIER.RARE),
        ],
    ),
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in legendary
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.EPIC),
            ],
        )
        for base_type in epic
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for base_type in rare
    ],
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Divination Cards"),
            extensions.DefaultStyle(),
        ],
    ),
]
