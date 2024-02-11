from app import builds, common, filter

rules = [
    *builds.rules,
    *common.rules,
]

filter.generate(rules=rules, filter_name="main")
