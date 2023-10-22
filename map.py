import rule
import categories


class MapStyle(rule.Rule):
    def label(self) -> categories.LABEL:
        return categories.LABEL.WHITE_ON_RED

    def icon_shape(self) -> categories.SHAPE:
        return categories.SHAPE.CIRCLE


class Map(MapStyle):
    def __init__(self, tier: str = "> 0", **kwargs):
        super().__init__(**kwargs)
        self.tier = tier

    def filter(self):
        return f"""
            Class == "Maps"
            MapTier {self.tier}
        """


class InfluencedMap(MapStyle):
    def filter(self):
        return """
            Class == "Maps"
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


rules = [
    InfluencedMap(
        rarity=categories.RARITY.LEGENDARY,
    ),
    Map(
        rarity=categories.RARITY.EPIC,
        tier="== 16",
    ),
    Map(
        rarity=categories.RARITY.RARE,
        strictness=categories.STRICTNESS.STRICT,
        tier="< 16",
    ),
]
