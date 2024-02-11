from app import categories, extensions
from app.rules import Rule


best_in_slot_items = [
    "Foliate Brooch",
    "Whisper-woven Cloak",
    "Precise Arrowhead",
    # Tools
    "Regicide Disguise Kit",
    "Grandmaster Keyring",
    "Thaumetic Flashpowder",
    "Thaumaturgical Sensing Charm",
    "Thaumaturgical Ward",
    "Silkweave Sole",
    "Thaumetic Blowtorch",
    "Steel Bracers",
    "Master Lockpick",
]
heist_classes = [
    "Heist Brooch",
    "Heist Cloak",
    "Heist Gear",
    "Heist Tool",
    "Heist Target",
]


rules = [
    # Tiered bases
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.ItemLevel(item_level=83, operator=categories.OPERATOR.GTE),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in best_in_slot_items
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for class_name in heist_classes
    ],
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Blueprint"),
            extensions.ItemLevel(item_level=83, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Contract"),
            extensions.ItemLevel(item_level=83, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Blueprint"),
            extensions.ItemLevel(item_level=68, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Contract"),
            extensions.ItemLevel(item_level=68, operator=categories.OPERATOR.GTE),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name="Trinket"),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Tailoring Orb"),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Tempering Orb"),
            extensions.TierStyle(tier=categories.TIER.LEGENDARY),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.BaseType(base_type="Rogue's Marker"),
            extensions.TierStyle(tier=categories.TIER.COMMON),
        ],
    ),
]
