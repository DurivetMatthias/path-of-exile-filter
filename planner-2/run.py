from app.build_file import BuildFile, generate
from app.skills import Skill, Support

items = []

passives = []

skills = [
    # Boneshatter setup
    Skill(
        "Metadata/Items/Gem/SkillGemPlayerDefaultUnarmed",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemBrink"),
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
        ],
    ),
    Skill(
        "Metadata/Items/Gem/SkillGemRollingSlam",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemBrink"),
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
        ],
    ),
    Skill(
        "Metadata/Items/Gem/SkillGemBoneshatter",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemImpactShockwave"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
        ],
    ),
    # Shield Wall
    Skill(
        "Metadata/Items/Gems/SkillGemShieldWall",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
            Support("Metadata/Items/Gems/SupportGemMartialTempoTwo"),
            Support("Metadata/Items/Gems/SupportGemMartialTempoThree"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectThree"),
            Support("Metadata/Items/Gems/SupportGemConcentratedEffect"),
            Support("Metadata/Items/Gems/SupportGemImpale"),
            Support("Metadata/Items/Gems/SupportGemHeft"),
            Support("Metadata/Items/Gems/SupportGemLacerate"),
            Support("Metadata/Items/Gems/SupportGemLacerateTwo"),
            Support("Metadata/Items/Gems/SupportGemLacerateThree"),
            Support("Metadata/Items/Gems/SupportGemLacerateFour"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemInfernalCry",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemRagingCry"),
            Support("Metadata/Items/Gems/SupportGemTireless"),
            Support("Metadata/Items/Gems/SupportGemEchoingCry"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectThree"),
            Support("Metadata/Items/Gems/SupportGemCorruptingCry"),
            Support("Metadata/Items/Gems/SupportGemCorruptingCryTwo"),
            Support("Metadata/Items/Gems/SupportGemCorruptingCryThree"),
        ],
    ),
    Skill(  # Human version
        "Metadata/Items/Gems/SkillGemFortifyingCry",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemRagingCry"),
            Support("Metadata/Items/Gems/SupportGemBrutality"),
            Support("Metadata/Items/Gems/SupportGemBrutalityTwo"),
            Support("Metadata/Items/Gems/SupportGemBrutalityThree"),
            Support("Metadata/Items/Gems/SupportGemHeft"),
            Support("Metadata/Items/Gems/SupportGemHeavySwing"),
            Support("Metadata/Items/Gems/SupportGemInspiration"),
            Support("Metadata/Items/Gems/SupportGemInspirationTwo"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemHeraldOfAsh",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemPersistenceThree"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectThree"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemWarBanner",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemPersistenceThree"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectThree"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemScavengedPlating",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemPersistenceThree"),
            Support("Metadata/Items/Gems/SupportGemClarity"),
        ],
    ),
]

build_file = BuildFile(
    name="Shield Wall Leveling",
    description="Level as Boneshatter, transition into shield wall.",
    ascendancy="Warrior2",
    items=items,
    passives=passives,
    skills=skills,
)

generate("shield-wall", build_file)
