"""This file defines the rules for divinations cards."""

import categories
import rule


class Card(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_BLUE

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.SQUARE


# Cards with extremely valuable rewards
legendary_cards = [
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
]

# Cards with useful results
epic_cards = [
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
]

# Rare cards that give an interesting reward
rare_cards = [
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
    "The Price of Prescience",
    "The Price of Protection",
    "The Professor",
    "The Risk",
    "The Scholar",
    "The Twilight Moon",
    "Vanity",
]

bad_cards = [
    "A Chilling Wind",
    "A Dab of Ink",
    "A Familiar Call",
    "A Mother's Parting Gift",
    "A Note in the Wind",
    "Akil's Prophecy",
    "Alivia's Grace",
    "Alone in the Darkness",
    "Anarchy's Price",
    "Assassin's Favour",
    "Astral Protection",
    "Atziri's Arsenal",
    "Audacity",
    "Azure Rage",
    "Beauty Through Death",
    "Blind Venture",
    "Boon of Justice",
    "Boon of the First Ones",
    "Boundless Realms",
    "Bowyer's Dream",
    "Broken Promises",
    "Broken Truce",
    "Brotherhood in Exile",
    "Buried Treasure",
    "Burning Blood",
    "Call to the First Ones",
    "Cartographer's Delight",
    "Choking Guilt",
    "Council of Cats",
    "Cursed Words",
    "Dark Dreams",
    "Dark Temptation",
    "Deadly Joy",
    "Death",
    "Desperate Crusade",
    "Dialla's Subjugation",
    "Divine Justice",
    "Doedre's Madness",
    "Draped in Dreams",
    "Dying Anguish",
    "Dying Light",
    "Earth Drinker",
    "Echoes of Love",
    "Emperor of Purity",
    "Emperor's Luck",
    "Endless Night",
    "Etched in Blood",
    "Fateful Meeting",
    "Fire Of Unknown Origin",
    "Forbidden Power",
    "From Bone to Ashes",
    "Further Invention",
    "Gemcutter's Promise",
    "Gift of Asenath",
    "Gift of the Gemling Queen",
    "Haunting Shadows",
    "Her Mask",
    "Heterochromia",
    "His Judgement",
    "Hope",
    "Hubris",
    "Hunter's Resolve",
    "Hunter's Reward",
    "Immortal Resolve",
    "Imperial Legacy",
    "Jack in the Box",
    "Justified Ambition",
    "Lantador's Lost Love",
    "Left to Fate",
    "Lethean Temptation",
    "Light and Truth",
    "Lost Worlds",
    "Love Through Ice",
    "Loyalty",
    "Lysah's Respite",
    "Mawr Blaidd",
    "Merciless Armament",
    "Might is Right",
    "Misery in Darkness",
    "Mitts",
    "Parasitic Passengers",
    "Perfection",
    "Poisoned Faith",
    "Prejudice",
    "Pride Before the Fall",
    "Pride of the First Ones",
    "Prometheus' Armoury",
    "Prosperity",
    "Rain of Chaos",
    "Rain Tempter",
    "Rats",
    "Rebirth",
    "Reckless Ambition",
    "Remembrance",
    "Sambodhi's Wisdom",
    "Silence and Frost",
    "Soul Quenched",
    "Struck by Lightning",
    "Succor of the Sinless",
    "Terrible Secret of Space",
    "The Academic",
    "The Admirer",
    "The Adventuring Spirit",
    "The Aesthete",
    "The Archmage's Right Hand",
    "The Arena Champion",
    "The Army of Blood",
    "The Aspirant",
    "The Astromancer",
    "The Avenger",
    "The Awakened",
    "The Battle Born",
    "The Bear Woman",
    "The Beast",
    "The Betrayal",
    "The Bitter Blossom",
    "The Blazing Fire",
    "The Blessing of Moosh",
    "The Body",
    "The Bones",
    "The Brawny Battle Mage",
    "The Breach",
    "The Brittle Emperor",
    "The Calling",
    "The Carrion Crow",
    "The Cataclysm",
    "The Catalyst",
    "The Celestial Justicar",
    "The Celestial Stone",
    "The Chosen",
    "The Coming Storm",
    "The Conduit",
    "The Craving",
    "The Cursed King",
    "The Damned",
    "The Dark Mage",
    "The Darkest Dream",
    "The Deceiver",
    "The Deep Ones",
    "The Demoness",
    "The Doppelganger",
    "The Dragon",
    "The Dreamer",
    "The Drunken Aristocrat",
    "The Dungeon Master",
    "The Emptiness",
    "The Endless Darkness",
    "The Enforcer",
    "The Enthusiasts",
    "The Escape",
    "The Ethereal",
    "The Explorer",
    "The Eye of Terror",
    "The Fathomless Depths",
    "The Feast",
    "The Fletcher",
    "The Flora's Gift",
    "The Fool",
    "The Forgotten Treasure",
    "The Formless Sea",
    "The Forsaken",
    "The Forward Gaze",
    "The Fox",
    "The Fox in the Brambles",
    "The Gambler",
    "The Gemcutter",
    "The Gentleman",
    "The Gladiator",
    "The Golden Era",
    "The Greatest Intentions",
    "The Gulf",
    "The Hale Heart",
    "The Harvester",
    "The Hermit",
    "The Hive of Knowledge",
    "The Hook",
    "The Hunger",
    "The Incantation",
    "The Inoculated",
    "The Insatiable",
    "The Jester",
    "The Jeweller's Boon",
    "The Journalist",
    "The King's Blade",
    "The King's Heart",
    "The Last One Standing",
    "The Last Supper",
    "The Lich",
    "The Life Thief",
    "The Lion",
    "The Lord in Black",
    "The Lord of Celebration",
    "The Lover",
    "The Lunaris Priestess",
    "The Mad King",
    "The Master",
    "The Mercenary",
    "The Messenger",
    "The Metalsmith's Gift",
    "The Mind's Eyes",
    "The Mountain",
    "The Oath",
    "The Offering",
    "The Offspring",
    "The One That Got Away",
    "The One With All",
    "The Opulent",
    "The Pack Leader",
    "The Pact",
    "The Penitent",
    "The Poet",
    "The Polymath",
    "The Porcupine",
    "The Price of Loyalty",
    "The Primordial",
    "The Prince of Darkness",
    "The Progeny of Lunaris",
    "The Queen",
    "The Rabbit's Foot",
    "The Rabid Rhoa",
    "The Realm",
    "The Return of the Rat",
    "The Rite of Elements",
    "The Road to Power",
    "The Ruthless Ceinture",
    "The Sacrifice",
    "The Scarred Meadow",
    "The Scavenger",
    "The Shepherd's Sandals",
    "The Shieldbearer",
    "The Sigil",
    "The Siren",
    "The Skeleton",
    "The Soul",
    "The Spark and the Flame",
    "The Spoiled Prince",
    "The Standoff",
    "The Stormcaller",
    "The Strategist",
    "The Summoner",
    "The Sun",
    "The Surgeon",
    "The Surveyor",
    "The Survivalist",
    "The Sword King's Salute",
    "The Thaumaturgist",
    "The Throne",
    "The Tower",
    "The Traitor",
    "The Trial",
    "The Tumbleweed",
    "The Twins",
    "The Tyrant",
    "The Undaunted",
    "The Undisputed",
    "The Unexpected Prize",
    "The Valkyrie",
    "The Vast",
    "The Visionary",
    "The Warden",
    "The Warlord",
    "The Watcher",
    "The Web",
    "The Wedding Gift",
    "The White Knight",
    "The Whiteout",
    "The Wilted Rose",
    "The Wind",
    "The Witch",
    "The Wolf",
    "The Wolf's Legacy",
    "The Wolf's Shadow",
    "The Wolven King's Bite",
    "The Wolverine",
    "The World Eater",
    "The Wretched",
    "Thirst for Knowledge",
    "Thunderous Skies",
    "Time-Lost Relic",
    "Tranquillity",
    "Treasure Hunter",
    "Triskaidekaphobia",
    "Turn the Other Cheek",
    "Unchained",
    "Vile Power",
    "Void of the Elements",
    "Volatile Power",
    "Winter's Embrace",
]

rules = [
    Card(
        name="Stacked Deck",
        rarity=categories.RARITY.RARE,
    ),
    *[
        Card(
            name=card_name,
            rarity=categories.RARITY.LEGENDARY,
        )
        for card_name in legendary_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=categories.RARITY.EPIC,
        )
        for card_name in epic_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=categories.RARITY.RARE,
            strictness=categories.STRICTNESS.STRICT,
        )
        for card_name in rare_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=categories.RARITY.COMMON,
            hide=True,
        )
        for card_name in bad_cards
    ],
]
