from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

exceptional_gems = [
    "Empower Support",
    "Enlighten Support",
    "Enhance Support",
]
rules = [
    Show(
        [
            MultiBaseType(exceptional_gems),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Show(
        [
            Class("Support Gems"),
            BaseType("Awakened", OPERATOR.CONTAINS),
            TierStyle(TIER.LEGENDARY),
        ],
    ),
    Hide(
        [
            Class("Support Gems"),
        ]
    ),
    Hide(
        [
            Class("Skill Gems"),
        ]
    ),
]
fire_gems = [
    "Alchemist's Mark",
    "Artillery Ballista",
    "Blast Rain",
    "Burning Arrow",
    "Cremation",
    "Detonate Dead",
    "Elemental Hit",
    "Explosive Arrow",
    "Explosive Concoction",
    "Explosive Trap",
    "Fire Trap",
    "Flamethrower Trap",
    "Vaal Burning Arrow",
    "Vaal Detonate Dead",
    "Volatile Dead",
    "Wild Strike",
    "Armageddon Brand",
    "Blazing Salvo",
    "Bodyswap",
    "Discharge",
    "Fireball",
    "Firestorm",
    "Flame Dash",
    "Flame Surge",
    "Flame Wall",
    "Flameblast",
    "Flammability",
    "Incinerate",
    "Purifying Flame",
    "Pyroclast Mine",
    "Righteous Fire",
    "Rolling Magma",
    "Scorching Ray",
    "Summon Raging Spirit",
    "Vaal Fireball",
    "Vaal Firestorm",
    "Vaal Flameblast",
    "Vaal Righteous Fire",
    "Anger",
    "Consecrated Path",
    "Flame Link",
    "Holy Flame Totem",
    "Infernal Blow",
    "Infernal Cry",
    "Molten Shell",
    "Molten Strike",
    "Searing Bond",
    "Summon Flame Golem",
    "Tectonic Slam",
    "Vaal Molten Shell",
    "Vaal Molten Strike",
    "Vaal Volcanic Fissure",
    "Volcanic Fissure",
    "Combustion Support",
    "Elemental Proliferation Support",
    "Ignite Proliferation Support",
    "Immolate Support",
    "Infernal Legion Support",
    "Prismatic Burst Support",
    "Added Fire Damage Support",
    "Awakened Added Fire Damage Support",
    "Awakened Burning Damage Support",
    "Awakened Fire Penetration Support",
    "Burning Damage Support",
    "Cold to Fire Support",
    "Controlled Blaze Support",
    "Fire Penetration Support",
    "Flamewood Support",
]
rules.append(
    Show(
        [
            MultiBaseType(fire_gems),
            Quality(),
            TierStyle(TIER.RARE),
        ]
    )
)
