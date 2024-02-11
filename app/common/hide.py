from app import classes, extensions, rules

rules = [
    *[
        rules.Rule(
            instruction=extensions.Hide(),
            extensions=[extensions.ClassName(class_name=class_name)],
        )
        for class_name in classes.GEAR
    ],
]
