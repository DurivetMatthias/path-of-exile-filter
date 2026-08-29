from app import filter
from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *

# Sections
from sections import (
    amulet,
    belt,
    boots,
    currency,
    flask,
    gem,
    gloves,
    helmet,
    jewel,
    mace,
    other,
    ring,
    shield,
    body,
    waystone,
)

rules = [
    *currency.rules,
    *flask.rules,
    *gem.rules,
    *jewel.rules,
    *waystone.rules,
    *other.rules,
    *belt.rules,
    *amulet.rules,
    *ring.rules,
    *helmet.rules,
    *boots.rules,
    *gloves.rules,
    *shield.rules,
    *body.rules,
    *mace.rules,
]

filter.generate(rules, "shield-wall")
