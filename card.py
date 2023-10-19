from rule import Rule
import rarity_options


class Card(Rule):
    def label(self) -> str:
        return """
            SetFontSize 45
            SetTextColor 0 0 0
            SetBackgroundColor 150 150 255
            SetBorderColor 150 150 255
        """

    def sound(self) -> str:
        return """
            DisableDropSound
            CustomAlertSound "filter-sounds/lily-sniff.mp3"
        """

    def icon(self) -> str:
        """Customize the look of the map icon that appears in-game"""
        if self.rarity == rarity_options.COMMON:
            return "MinimapIcon 2 White Square"
        if self.rarity == rarity_options.RARE:
            return "MinimapIcon 2 Blue Square"
        if self.rarity == rarity_options.EPIC:
            return "MinimapIcon 1 Purple Square"
        if self.rarity == rarity_options.LEGENDARY:
            return "MinimapIcon 0 Orange Square"
        return "MinimapIcon -1"


legendary_cards = [
    "Brother's Gift",
    "Brother's Stash",
    "Divine Beauty",
    "Home",
    "The Dragon's Heart",
    "Abandoned Wealth",
    "Alluring Bounty",
    "The Hoarder",
    "The Saint's Treasure",
    "The Fortunate",
    "The Sephirot",
    "The Long Con",
    "The Scout",
    "Demigod's Wager",
    "The Seeker",
    "Darker Half",
    "The Artist",
    "Gemcutter's Mercy",
    "The Enlightened",
    "Wealth and Power",
    "House of Mirrors",
    "Lachrymal Necrosis",
    "Peaceful Moments",
    "Rebirth and Renewal",
    "The Cheater",
    "The Demon",
    "The Destination",
    "The Eternal War",
    "The Eye of the Dragon",
    "The Garish Power",
    "The Innocent",
    "The Immortal",
    "The Insane Cat",
    "The Price of Devotion",
    "The Shortcut",
    "Unrequited Love",
]


epic_cards = [
    "Chaotic Disposition",
    "No Traces",
    "The Cache",
    "Ever-Changing",
    "Monochrome",
    "The Risk",
    "The Professor",
    "The Primordial",
    "The Nurse",
    "The Patient",
    "The Magma Crab",
    "The Samurai's Eye",
    "The Side Quest",
    "The Twilight Moon",
    "The Wolf's Legacy",
    "Treasure Hunter",
]


rare_cards = [
    "Destined to Crumble",
    "The Endurance",
    "Shard of Fate",
    "A Sea of Blue",
    "The Cartographer",
    "Society's Remorse",
    "Stacked Deck",
    "The Void",
    "The Finishing Touch",
    "Vinia's Token",
    "A Fate Worse Than Death",
    "Acclimatisation",
    "Vanity",
    "Humility",
    "Guardian's Challenge",
    "Justified Ambition",
    "The Encroaching Darkness",
    "The Easy Stroll",
    "The Price of Protection",
    "Triskaidekaphobia",
]

bad_cards = [
    "Alone in the Darkness",
    "Boon of Justice",
    "Dark Temptation",
    "Earth Drinker",
    "Gemcutter's Promise",
    "Her Mask",
    "Rain of Chaos",
    "Doedre's Madness",
    "Emperor's Luck",
    "Hubris",
    "Hunter's Resolve",
    "Imperial Legacy",
    "Lantador's Lost Love",
    "Loyalty",
    "Mitts",
    "Prosperity",
    "The Battle Born",
    "Struck by Lightning",
    "The Adventuring Spirit",
    "The Aesthete",
    "The Blazing Fire",
    "The Calling",
    "The Carrion Crow",
    "The Catalyst",
    "The Coming Storm",
    "The Demoness",
    "The Doppelganger",
    "The Dragon",
    "The Flora's Gift",
    "The Gambler",
    "The Gemcutter",
    "The Harvester",
    "The Hermit",
    "The Journalist",
    "The King's Blade",
    "The Lion",
    "The Lover",
    "The Lunaris Priestess",
    "The Metalsmith's Gift",
    "The Mountain",
    "The Penitent",
    "The Porcupine",
    "The Realm",
    "The Skeleton",
    "The Rite of Elements",
    "The Summoner",
    "The Sun",
    "The Surgeon",
    "The Sword King's Salute",
    "The Tower",
    "Thunderous Skies",
    "Time-Lost Relic",
    "Volatile Power",
    "The Body",
]

rules = [
    *[
        Card(
            name=card_name,
            rarity=rarity_options.LEGENDARY,
        )
        for card_name in legendary_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=rarity_options.EPIC,
        )
        for card_name in epic_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=rarity_options.RARE,
        )
        for card_name in rare_cards
    ],
    *[
        Card(
            name=card_name,
            rarity=rarity_options.COMMON,
            hide=True,
        )
        for card_name in bad_cards
    ],
]
