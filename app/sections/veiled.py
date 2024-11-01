from app.blocks import Show
from app.conditions import VeiledPrefix, VeiledSuffix

rules = [
    Show([VeiledPrefix()]),
    Show([VeiledSuffix()]),
]
