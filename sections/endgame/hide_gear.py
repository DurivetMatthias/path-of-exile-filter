from app.blocks import *
from app.actions import *
from app.base_types import *
from app.categories import *
from app.conditions import *

rules = [
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([JewelryClasses()]),
    Hide([FlaskClasses()]),
]
