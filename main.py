from app import common, filter

rules = [
    *common.rules,
]

filter.generate(rules=rules, filter_name="main")
