from rule import Rule


class HideRule(Rule):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, hide=True, **kwargs)


class HideClass(HideRule):
    def filter(self):
        return f"""
            Class == "{self.name}"
        """


class HideItem(HideRule):
    def filter(self):
        return f"""
            BaseType == "{self.name}"
        """


partial_classes = [
    "Sceptres",
    "Amulets",
    "Rings",
    "Gloves",
    "Boots",
    "Belts",
    "Helmets",
    "Body Armours",
    "Jewels",
    "Utility Flasks",
    "Life Flasks",
]
bad_classes = [
    "Mana Flasks",
    "Hybrid Flasks",
    "Quivers",
    "One Hand Axes",
    "Two Hand Axes",
    "Rune Daggers",
    "Daggers",
    "Claws",
    "One Hand Swords",
    "Two Hand Swords",
    "Thrusting One Hand Swords",
    "Staves",
    "Warstaves",
    "Shields",
    "One Hand Maces",
    "Two Hand Maces",
    "Bows",
    "Wands",
]

rules = [
    *[HideClass(name=class_name) for class_name in partial_classes],
    *[HideClass(name=class_name) for class_name in bad_classes],
]
