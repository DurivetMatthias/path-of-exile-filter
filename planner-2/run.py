from app.build_file import BuildFile, generate
from app.skills import Skill, Support

items = []

passives = []

skills = [
    # Boneshatter setup
    Skill(
        "Metadata/Items/Gem/SkillGemPlayerDefault1HMace",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gem/SupportGemBrink"),
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemRollingSlam",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gem/SupportGemBrink"),
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemBoneshatter",
        level_interval=[1, 21],
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemImpactShockwave"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
        ],
    ),
    # Shield Wall
    Skill(
        "Metadata/Items/Gem/SkillGemShieldWall",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemMartialTempo"),
            Support("Metadata/Items/Gems/SupportGemMartialTempoTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemConcentratedEffect"),
            Support("Metadata/Items/Gem/SupportGemImpale"),
            Support("Metadata/Items/Gem/SupportGemHeft"),
            Support("Metadata/Items/Gems/SupportGemLacerate"),
            Support("Metadata/Items/Gems/SupportGemLacerateTwo"),
            Support("Metadata/Items/Gems/SupportGemLacerateThree"),
            Support("Metadata/Items/Gems/SupportGemLacerateFour"),
            # Lineage
            Support("Metadata/Items/Gems/SupportGemAhnsCitadel"),
            Support("Metadata/Items/Gems/SupportGemAtaluiBloodletting"),
            Support("Metadata/Items/Gem/SupportGemKaomsMadness"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemInfernalCry",
        support_skills=[
            Support("Metadata/Items/Gem/SupportGemRagingCry"),
            Support("Metadata/Items/Gems/SupportGemEnragedWarcry"),
            Support("Metadata/Items/Gems/SupportGemEnragedWarcryTwo"),
            Support("Metadata/Items/Gem/SupportGemTireless"),
            Support("Metadata/Items/Gems/SupportGemEchoingCry"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemLifetap"),
        ],
    ),
    Skill(
        "Metadata/Items/Gem/SkillGemFortifyingCry",
        support_skills=[
            Support("Metadata/Items/Gem/SupportGemRagingCry"),
            Support("Metadata/Items/Gems/SupportGemEnragedWarcry"),
            Support("Metadata/Items/Gems/SupportGemEnragedWarcryTwo"),
            Support("Metadata/Items/Gems/SupportGemBrutality"),
            Support("Metadata/Items/Gems/SupportGemBrutalityTwo"),
            Support("Metadata/Items/Gems/SupportGemBrutalityThree"),
            Support("Metadata/Items/Gem/SupportGemHeft"),
            Support("Metadata/Items/Gems/SupportGemHeavySwing"),
            Support("Metadata/Items/Gems/SupportGemInspiration"),
            Support("Metadata/Items/Gems/SupportGemInspirationTwo"),
            Support("Metadata/Items/Gems/SupportGemLifetap"),
        ],
    ),
    Skill(
        "Metadata/Items/Gems/SkillGemSunder",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemRageThree"),
            Support("Metadata/Items/Gems/SupportGemMartialTempoThree"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
        ],
    ),
    # Spirit gems
    Skill(
        "Metadata/Items/Gems/SkillGemHeraldOfAsh",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gems/SupportGemFireMastery"),
        ],
    ),
    Skill(
        "Metadata/Items/Gem/SkillGemWarBanner",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffect"),
            Support("Metadata/Items/Gems/SupportGemMagnifiedEffectTwo"),
            Support("Metadata/Items/Gem/SupportGemDaressosPassion"),
        ],
    ),
    Skill(
        "Metadata/Items/Gem/SkillGemScavengedPlating",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistence"),
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
            Support("Metadata/Items/Gems/SupportGemClarity"),
        ],
    ),
    # Movement
    Skill(
        "Metadata/Items/Gems/SkillGemLeapSlam",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemRageThree"),
            Support("Metadata/Items/Gems/SupportGemMartialTempoThree"),
        ],
    ),
    # Utility
    Skill(
        "Metadata/Items/Gem/SkillGemTameBeast",
        support_skills=[
            Support("Metadata/Items/Gems/SupportGemPersistenceTwo"),
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
