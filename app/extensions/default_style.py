from app import extensions


class DefaultStyle(extensions.Extension):
    """
    This extensions serves as an explicit indicator that a specific rule is
    leveraging parts of the default style.
    For example, veiled items will have a veiled symbol, normal, magic and rare
    items will have the appropriate text color.
    Other extensions do overwrite specific parts of the style that they overwrite.
    """

    def __str__(self):
        return ""
