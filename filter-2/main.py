from app import filter
from app.actions import *
from app.blocks import *
from app.categories import *
from app.conditions import *
from app.styles import *
from sections.campaign import currency as campaign_currency
from sections.campaign import flask as campaign_flask
from sections.campaign import gem as campaign_gem
from sections.campaign import jewel as campaign_jewel
from sections.campaign import other as campaign_other
from sections.campaign import unique as campaign_unique
from sections.campaign.builds import shield_wall as campaign_shield_wall
from sections.endgame import currency as endgame_currency
from sections.endgame import flask as endgame_flask
from sections.endgame import gem as endgame_gem
from sections.endgame import jewel as endgame_jewel
from sections.endgame import other as endgame_other
from sections.endgame import unique as endgame_unique
from sections.endgame.builds import shield_wall as endgame_shield_wall

campaign_rules = [
    *campaign_gem.rules,
    *campaign_flask.rules,
    *campaign_jewel.rules,
    *campaign_other.rules,
    *campaign_unique.rules,
    *campaign_currency.rules,
    *campaign_shield_wall.rules,
]

for rule in campaign_rules:
    rule.conditions.append(AreaLevel(65, OPERATOR.LT))

endgame_rules = [
    *endgame_gem.rules,
    *endgame_flask.rules,
    *endgame_jewel.rules,
    *endgame_other.rules,
    *endgame_unique.rules,
    *endgame_currency.rules,
    *endgame_shield_wall.rules,
]

rules = [
    *campaign_rules,
    *endgame_rules,
]

filter.generate(rules, "shield-wall")
