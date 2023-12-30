from app import categories, extensions
from app.rules import Rule

style_extensions = [
    extensions.DefaultStyle(),
]

rules = [
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledPrefix(),
            *style_extensions,
        ],
    ),
    Rule(
        instruction=extensions.Show(),
        extensions=[
            extensions.VeiledSuffix(),
            *style_extensions,
        ],
    ),
]
