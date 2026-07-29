from app import filter
from data_collection import currency_with_sounds

rules = [*currency_with_sounds.rules]

filter.generate(rules=rules, name="data-collection")
