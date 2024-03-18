from app import categories, classes, extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.ClassName(class_name=classes.MAPS),
            extensions.TierStyle(tier=categories.TIER.EPIC),
        ],
    ),
]
