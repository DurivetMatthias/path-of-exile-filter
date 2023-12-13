from app import categories, extensions
from app.rules import Rule


best_in_slot_items = [
    # Brooch
    "Foliate Brooch",
    # Cloak
    "Whisper-woven Cloak",
    # Gear
    "Precise Arrowhead",
    # Tool
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

common_items = [
    "Rogue's Marker",
]

rare_classes = [
    "Heist Brooch",
    "Heist Cloak",
    "Heist Gear",
    "Heist Tool",
    "Heist Target",
]

epic_classes = [
    "Contract",
]

legendary_classes = [
    "Blueprint",
    "Trinket",
]
legendary_items = [
    "Tailoring Orb",
    "Tempering Orb",
]


rules = [
    # Tiered bases
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in best_in_slot_items
    ],
    # Tiered classes
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for class_name in legendary_classes
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.LEGENDARY),
            ],
        )
        for base_type in legendary_items
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.TierStyle(tier=categories.TIER.EPIC),
            ],
        )
        for class_name in epic_classes
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.TierStyle(tier=categories.TIER.RARE),
            ],
        )
        for class_name in rare_classes
    ],
    *[
        Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.BaseType(base_type=base_type),
                extensions.TierStyle(tier=categories.TIER.COMMON),
            ],
        )
        for base_type in common_items
    ],
]
