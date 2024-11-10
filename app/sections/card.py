from app.blocks import Hide, Show
from app.conditions import BaseType, MultiBaseType
from app.actions import TierStyle
from app.categories import TIER

HIDE = "hide"
COMMON = "common"
RARE = "rare"
EPIC = "epic"
LEGENDARY = "legendary"

cards = {
    "A Chilling Wind": HIDE,
    "A Dab of Ink": HIDE,
    "A Dusty Memory": HIDE,
    "A Familiar Call": HIDE,
    "A Fate Worse Than Death": LEGENDARY,
    "A Modest Request": LEGENDARY,
    "A Mother's Parting Gift": HIDE,
    "A Note in the Wind": HIDE,
    "A Sea of Blue": RARE,
    "A Stone Perfected": LEGENDARY,
    "Abandoned Wealth": LEGENDARY,
    "Acclimatisation": RARE,
    "Akil's Prophecy": HIDE,
    "Alivia's Grace": HIDE,
    "Alluring Bounty": LEGENDARY,
    "Alone in the Darkness": HIDE,
    "Altered Perception": LEGENDARY,
    "Ambitious Obsession": RARE,
    "Anarchy's Price": HIDE,
    "Arrogance of the Vaal": LEGENDARY,
    "Assassin's Favour": HIDE,
    "Assassin's Gift": HIDE,
    "Astral Protection": HIDE,
    "Atziri's Arsenal": HIDE,
    "Audacity": HIDE,
    "Auspicious Ambitions": LEGENDARY,
    "Avian Pursuit": LEGENDARY,
    "Azure Rage": HIDE,
    "Azyran's Reward": LEGENDARY,
    "Baited Expectations": LEGENDARY,
    "Beauty Through Death": HIDE,
    "Bijoux": LEGENDARY,
    "Blind Venture": HIDE,
    "Boon of Justice": HIDE,
    "Boon of the First Ones": HIDE,
    "Boundless Realms": HIDE,
    "Bowyer's Dream": HIDE,
    "Broken Promises": LEGENDARY,
    "Broken Truce": HIDE,
    "Brother's Gift": LEGENDARY,
    "Brother's Stash": LEGENDARY,
    "Brotherhood in Exile": HIDE,
    "Brush, Paint and Palette": LEGENDARY,
    "Buried Treasure": RARE,
    "Burning Blood": HIDE,
    "Call to the First Ones": HIDE,
    "Cameria's Cut": RARE,
    "Cartographer's Delight": HIDE,
    "Chaotic Disposition": EPIC,
    "Chasing Risk": LEGENDARY,
    "Checkmate": LEGENDARY,
    "Choking Guilt": HIDE,
    "Costly Curio": LEGENDARY,
    "Council of Cats": HIDE,
    "Coveted Possession": RARE,
    "Cursed Words": HIDE,
    "Dark Dreams": LEGENDARY,
    "Dark Temptation": HIDE,
    "Darker Half": LEGENDARY,
    "Deadly Joy": HIDE,
    "Death": HIDE,
    "Deathly Designs": LEGENDARY,
    "Dementophobia": LEGENDARY,
    "Demigod's Wager": LEGENDARY,
    "Desecrated Virtue": LEGENDARY,
    "Desperate Crusade": LEGENDARY,
    "Destined to Crumble": HIDE,
    "Dialla's Subjugation": HIDE,
    "Disdain": RARE,
    "Divine Beauty": LEGENDARY,
    "Doedre's Madness": HIDE,
    "Draped in Dreams": HIDE,
    "Duality": HIDE,
    "Dying Light": HIDE,
    "Earth Drinker": HIDE,
    "Echoes of Love": HIDE,
    "Eldritch Perfection": LEGENDARY,
    "Emperor of Purity": HIDE,
    "Emperor's Luck": HIDE,
    "Endless Night": HIDE,
    "Etched in Blood": HIDE,
    "Eternal Bonds": LEGENDARY,
    "Ever-Changing": LEGENDARY,
    "Fateful Meeting": LEGENDARY,
    "Fire Of Unknown Origin": LEGENDARY,
    "Forbidden Power": HIDE,
    "From Bone to Ashes": LEGENDARY,
    "Further Invention": LEGENDARY,
    "Gemcutter's Mercy": LEGENDARY,
    "Gemcutter's Promise": HIDE,
    "Gift of Asenath": LEGENDARY,
    "Gift of the Gemling Queen": HIDE,
    "Glimmer of Hope": HIDE,
    "Grave Knowledge": RARE,
    "Guardian's Challenge": LEGENDARY,
    "Harmony of Souls": LEGENDARY,
    "Haunting Shadows": HIDE,
    "Her Mask": HIDE,
    "Heterochromia": HIDE,
    "Home": LEGENDARY,
    "Hope": HIDE,
    "House of Mirrors": LEGENDARY,
    "Hubris": HIDE,
    "Humility": HIDE,
    "Hunter's Resolve": HIDE,
    "Hunter's Reward": LEGENDARY,
    "I See Brothers": LEGENDARY,
    "Immortal Resolve": HIDE,
    "Imperfect Memories": LEGENDARY,
    "Imperial Legacy": HIDE,
    "Jack in the Box": HIDE,
    "Judging Voices": LEGENDARY,
    "Justified Ambition": LEGENDARY,
    "Keeper's Corruption": LEGENDARY,
    "Lachrymal Necrosis": LEGENDARY,
    "Lantador's Lost Love": HIDE,
    "Last Hope": HIDE,
    "Left to Fate": HIDE,
    "Lethean Temptation": HIDE,
    "Light and Truth": HIDE,
    "Lingering Remnants": HIDE,
    "Lost Worlds": HIDE,
    "Love Through Ice": LEGENDARY,
    "Loyalty": HIDE,
    "Lonely Warrior": LEGENDARY,
    "Lucky Connections": RARE,
    "Lucky Deck": RARE,
    "Luminous Trove": LEGENDARY,
    "Lysah's Respite": HIDE,
    "Magnum Opus": LEGENDARY,
    "Man With Bear": RARE,
    "Matryoshka": RARE,
    "Mawr Blaidd": HIDE,
    "Merciless Armament": HIDE,
    "Might is Right": HIDE,
    "Misery in Darkness": LEGENDARY,
    "Mitts": HIDE,
    "More is never enough": EPIC,
    "No Traces": LEGENDARY,
    "Nook's Crown": LEGENDARY,
    "Parasitic Passengers": RARE,
    "Peaceful Moments": LEGENDARY,
    "Perfection": HIDE,
    "Poisoned Faith": LEGENDARY,
    "Prejudice": HIDE,
    "Pride Before the Fall": HIDE,
    "Pride of the First Ones": HIDE,
    "Prometheus' Armoury": HIDE,
    "Prosperity": HIDE,
    "Rain of Chaos": HIDE,
    "Rain Tempter": HIDE,
    "Rats": HIDE,
    "Rebirth": HIDE,
    "Rebirth and Renewal": EPIC,
    "Reckless Ambition": HIDE,
    "Remembrance": RARE,
    "Sambodhi's Vow": EPIC,
    "Sambodhi's Wisdom": HIDE,
    "Scholar of the Seas": HIDE,
    "Seven Years Bad Luck": LEGENDARY,
    "Shard of Fate": EPIC,
    "Silence and Frost": HIDE,
    "Society's Remorse": RARE,
    "Something Dark": LEGENDARY,
    "Soul Quenched": HIDE,
    "Struck by Lightning": HIDE,
    "Succor of the Sinless": LEGENDARY,
    "The Academic": LEGENDARY,
    "The Admirer": HIDE,
    "The Adventuring Spirit": HIDE,
    "The Aesthete": HIDE,
    "The Apothecary": LEGENDARY,
    "The Archmage's Right Hand": HIDE,
    "The Arena Champion": HIDE,
    "The Army of Blood": HIDE,
    "The Artist": LEGENDARY,
    "The Aspirant": RARE,
    "The Astromancer": LEGENDARY,
    "The Avenger": HIDE,
    "The Awakened": HIDE,
    "The Battle Born": HIDE,
    "The Bear Woman": HIDE,
    "The Beast": HIDE,
    "The Betrayal": HIDE,
    "The Bitter Blossom": HIDE,
    "The Blazing Fire": HIDE,
    "The Body": HIDE,
    "The Bones": HIDE,
    "The Brawny Battle Mage": HIDE,
    "The Breach": LEGENDARY,
    "The Brittle Emperor": HIDE,
    "The Cache": HIDE,
    "The Cacophony": LEGENDARY,
    "The Calling": HIDE,
    "The Card Sharp": RARE,
    "The Carrion Crow": HIDE,
    "The Cartographer": HIDE,
    "The Cataclysm": RARE,
    "The Catalyst": HIDE,
    "The Catch": LEGENDARY,
    "The Celestial Justicar": HIDE,
    "The Celestial Stone": HIDE,
    "The Chains that Bind": HIDE,
    "The Cheater": LEGENDARY,
    "The Chosen": LEGENDARY,
    "The Coming Storm": LEGENDARY,
    "The Conduit": HIDE,
    "The Craving": LEGENDARY,
    "The Cursed King": HIDE,
    "The Damned": HIDE,
    "The Dapper Prodigy": HIDE,
    "The Dark Mage": RARE,
    "The Darkest Dream": HIDE,
    "The Deal": RARE,
    "The Deceiver": HIDE,
    "The Deep Ones": HIDE,
    "The Demon": LEGENDARY,
    "The Demoness": HIDE,
    "The Destination": LEGENDARY,
    "The Doctor": LEGENDARY,
    "The Doppelganger": HIDE,
    "The Dragon": HIDE,
    "The Dragon's Heart": LEGENDARY,
    "The Dreamer": LEGENDARY,
    "The Dreamland": HIDE,
    "The Drunken Aristocrat": HIDE,
    "The Dungeon Master": HIDE,
    "The Easy Stroll": HIDE,
    "The Eldritch Decay": LEGENDARY,
    "The Emptiness": HIDE,
    "The Encroaching Darkness": HIDE,
    "The Endless Darkness": HIDE,
    "The Endurance": EPIC,
    "The Enforcer": HIDE,
    "The Enlightened": LEGENDARY,
    "The Enthusiasts": HIDE,
    "The Escape": LEGENDARY,
    "The Eternal War": LEGENDARY,
    "The Ethereal": HIDE,
    "The Explorer": HIDE,
    "The Eye of Terror": LEGENDARY,
    "The Eye of the Dragon": LEGENDARY,
    "The Fathomless Depths": HIDE,
    "The Feast": HIDE,
    "The Fiend": LEGENDARY,
    "The Finishing Touch": EPIC,
    "The Fishmonger": LEGENDARY,
    "The Fletcher": HIDE,
    "The Flora's Gift": HIDE,
    "The Fool": HIDE,
    "The Forgotten Treasure": RARE,
    "The Formless Sea": HIDE,
    "The Forsaken": HIDE,
    "The Fortunate": LEGENDARY,
    "The Forward Gaze": RARE,
    "The Fox": HIDE,
    "The Fox in the Brambles": HIDE,
    "The Gambler": HIDE,
    "The Garish Power": LEGENDARY,
    "The Gemcutter": HIDE,
    "The Gentleman": HIDE,
    "The Gladiator": HIDE,
    "The Golden Era": HIDE,
    "The Greatest Intentions": ChildProcessError,
    "The Gulf": LEGENDARY,
    "The Hale Heart": LEGENDARY,
    "The Harvester": HIDE,
    "The Hermit": HIDE,
    "The Heroic Shot": RARE,
    "The Hive of Knowledge": HIDE,
    "The Hoarder": LEGENDARY,
    "The Hook": LEGENDARY,
    "The Hunger": LEGENDARY,
    "The Immortal": LEGENDARY,
    "The Incantation": HIDE,
    "The Innocent": LEGENDARY,
    "The Inoculated": HIDE,
    "The Insane Cat": LEGENDARY,
    "The Insatiable": HIDE,
    "The Inventor": RARE,
    "The Jester": HIDE,
    "The Jeweller's Boon": HIDE,
    "The Journalist": HIDE,
    "The Journey": HIDE,
    "The King's Blade": HIDE,
    "The King's Heart": HIDE,
    "The Landing": LEGENDARY,
    "The Last One Standing": HIDE,
    "The Last Supper": HIDE,
    "The Leviathan": LEGENDARY,
    "The Lich": HIDE,
    "The Life Thief": HIDE,
    "The Lion": HIDE,
    "The Long Con": LEGENDARY,
    "The Lord in Black": HIDE,
    "The Lord of Celebration": HIDE,
    "The Lover": HIDE,
    "The Lunaris Priestess": HIDE,
    "The Mad King": LEGENDARY,
    "The Magma Crab": HIDE,
    "The Master": HIDE,
    "The Master Artisan": HIDE,
    "The Mercenary": HIDE,
    "The Messenger": LEGENDARY,
    "The Metalsmith's Gift": HIDE,
    "The Mind's Eyes": HIDE,
    "The Mountain": HIDE,
    "The Nurse": LEGENDARY,
    "The Oath": HIDE,
    "The Obscured": LEGENDARY,
    "The Offering": HIDE,
    "The Offspring": HIDE,
    "The Old Man": LEGENDARY,
    "The One That Got Away": HIDE,
    "The One With All": HIDE,
    "The Opulent": HIDE,
    "The Pack Leader": HIDE,
    "The Pact": HIDE,
    "The Patient": LEGENDARY,
    "The Penitent": RARE,
    "The Poet": HIDE,
    "The Polymath": LEGENDARY,
    "The Porcupine": HIDE,
    "The Price of Devotion": LEGENDARY,
    "The Price of Loyalty": LEGENDARY,
    "The Price of Prescience": LEGENDARY,
    "The Price of Protection": LEGENDARY,
    "The Primordial": LEGENDARY,
    "The Prince of Darkness": LEGENDARY,
    "The Professor": HIDE,
    "The Progeny of Lunaris": HIDE,
    "The Puzzle": HIDE,
    "The Queen": HIDE,
    "The Rabbit's Foot": LEGENDARY,
    "The Rabid Rhoa": HIDE,
    "The Realm": HIDE,
    "The Return of the Rat": HIDE,
    "The Risk": RARE,
    "The Rite of Elements": HIDE,
    "The Road to Power": HIDE,
    "The Rusted Bard": LEGENDARY,
    "The Ruthless Ceinture": HIDE,
    "The Sacrifice": HIDE,
    "The Saint's Treasure": LEGENDARY,
    "The Samurai's Eye": LEGENDARY,
    "The Scarred Meadow": HIDE,
    "The Scavenger": HIDE,
    "The Scholar": HIDE,
    "The Scout": LEGENDARY,
    "The Seeker": LEGENDARY,
    "The Sephirot": LEGENDARY,
    "The Shepherd's Sandals": LEGENDARY,
    "The Shieldbearer": LEGENDARY,
    "The Shortcut": LEGENDARY,
    "The Side Quest": EPIC,
    "The Sigil": HIDE,
    "The Siren": HIDE,
    "The Skeleton": HIDE,
    "The Soul": HIDE,
    "The Spark and the Flame": LEGENDARY,
    "The Spoiled Prince": HIDE,
    "The Standoff": HIDE,
    "The Stormcaller": HIDE,
    "The Strategist": LEGENDARY,
    "The Summoner": HIDE,
    "The Sun": RARE,
    "The Surgeon": HIDE,
    "The Surveyor": HIDE,
    "The Survivalist": HIDE,
    "The Sword King's Salute": HIDE,
    "The Thaumaturgist": HIDE,
    "The Throne": LEGENDARY,
    "The Tinkerer's Table": EPIC,
    "The Tireless Extractor": EPIC,
    "The Tower": HIDE,
    "The Traitor": HIDE,
    "The Transformation": LEGENDARY,
    "The Trial": HIDE,
    "The Tumbleweed": HIDE,
    "The Twilight Moon": HIDE,
    "The Twins": HIDE,
    "The Tyrant": HIDE,
    "The Undaunted": HIDE,
    "The Undisputed": HIDE,
    "The Unexpected Prize": HIDE,
    "The Union": RARE,
    "The Valkyrie": HIDE,
    "The Vast": HIDE,
    "The Visionary": HIDE,
    "The Void": HIDE,
    "The Warden": HIDE,
    "The Warlord": HIDE,
    "The Watcher": HIDE,
    "The Web": HIDE,
    "The Wedding Gift": LEGENDARY,
    "The White Knight": HIDE,
    "The Whiteout": HIDE,
    "The Wilted Rose": RARE,
    "The Wind": HIDE,
    "The Witch": HIDE,
    "The Wolf": HIDE,
    "The Wolf's Legacy": HIDE,
    "The Wolf's Shadow": HIDE,
    "The Wolven King's Bite": HIDE,
    "The Wolverine": HIDE,
    "The World Eater": HIDE,
    "The Wrath": HIDE,
    "The Wretched": RARE,
    "Thirst for Knowledge": HIDE,
    "Three Faces in the Dark": HIDE,
    "Three Voices": HIDE,
    "Thunderous Skies": HIDE,
    "Time-Lost Relic": HIDE,
    "Toxic tidings": HIDE,
    "Tranquillity": HIDE,
    "Treasure Hunter": HIDE,
    "Triskaidekaphobia": RARE,
    "Turn the Other Cheek": HIDE,
    "Unchained": HIDE,
    "Unrequited Love": LEGENDARY,
    "Vanity": HIDE,
    "Vile Power": HIDE,
    "Vinia's Token": EPIC,
    "Void of the Elements": HIDE,
    "Volatile Power": HIDE,
    "Wealth and Power": LEGENDARY,
    "Who Asked": HIDE,
    "Winter's Embrace": LEGENDARY,
}

hidden_cards = [
    card_name for (card_name, card_tier) in cards.items() if card_tier == HIDE
]
common_cards = [
    card_name for (card_name, card_tier) in cards.items() if card_tier == COMMON
]
rare_cards = [
    card_name for (card_name, card_tier) in cards.items() if card_tier == RARE
]
epic_cards = [
    card_name for (card_name, card_tier) in cards.items() if card_tier == EPIC
]
legendary_cards = [
    card_name for (card_name, card_tier) in cards.items() if card_tier == LEGENDARY
]


rules = [
    Show(
        [
            BaseType("Stacked Deck"),
            TierStyle(TIER.RARE),
        ],
    ),
    Hide(
        [
            MultiBaseType(hidden_cards),
        ],
    ),
    # Show(
    #     [
    #         MultiBaseType(common_cards),
    #         TierStyle(TIER.COMMON),
    #     ],
    # ),
    Show(
        [
            MultiBaseType(rare_cards),
            TierStyle(TIER.RARE),
        ],
    ),
    Show(
        [
            MultiBaseType(epic_cards),
            TierStyle(TIER.EPIC),
        ],
    ),
    Show(
        [
            MultiBaseType(legendary_cards),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
]
