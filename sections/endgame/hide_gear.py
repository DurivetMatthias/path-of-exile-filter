from app.blocks import *
from app.actions import *
from app.categories import *
from app.conditions import *

rules = [
    Hide([GearClasses()]),
    Hide([WeaponClasses()]),
    Hide([OffhandClasses()]),
    Hide([JewelryClasses()]),
    Hide([FlaskClasses()]),
]
