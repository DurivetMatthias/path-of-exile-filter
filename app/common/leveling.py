from app import categories, extensions, rules

classes_with_sockets = ["Body Armours", "Helmets", "Gloves", "Boots"]

# sockets, ilvl, act
# 1        1     Act 1
# 2        1     Act 1
# 3	       2     Act 1
# 4        25    Act 3
# 5        35    Act 4
# 6        50    Act 6/7

rules = [
    *[
        rules.Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.SocketGroup(sockets="4", operator=categories.OPERATOR.EXACT),
                extensions.AreaLevel(area_level=35, operator=categories.OPERATOR.LT),
            ],
        )
        for class_name in classes_with_sockets
    ],
    *[
        rules.Rule(
            instruction=extensions.Show(),
            extensions=[
                extensions.ClassName(class_name=class_name),
                extensions.SocketGroup(sockets="5", operator=categories.OPERATOR.EXACT),
                extensions.AreaLevel(area_level=50, operator=categories.OPERATOR.LT),
            ],
        )
        for class_name in classes_with_sockets
    ],
    # 6 Links are shown thanks to the vendor recipe
]
