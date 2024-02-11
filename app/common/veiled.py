from app import extensions
from app.rules import Rule

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledPrefix(),
            extensions.DefaultStyle(),
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledSuffix(),
            extensions.DefaultStyle(),
        ],
    ),
]
