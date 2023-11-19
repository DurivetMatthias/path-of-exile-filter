"""
Programmatically generate item filter files.
This project aims to simplify the configuration of colors, sounds, effects etc.
This is done by adding tags to all items and then applying rules to those tags.
In doing so we avoid the many to many assignment of properties and try to
reduce it to one-to-one as much as possible
"""
import os
import textwrap
import datetime

import categories
import config

import altered_bases
import card
import currency
import essence
import gear
import gem
import heist
import hidden
import map
import miscellaneous
import unique
import veiled


rules = [
    *unique.rules,
    *map.rules,
    *altered_bases.rules,
    *heist.rules,
    *veiled.rules,
    *gem.rules,
    *gear.rules,
    *currency.rules,
    *card.rules,
    *miscellaneous.rules,
    *essence.rules,
    *hidden.rules,
]

strictness_levels = [
    ("less-strict", categories.STRICTNESS.LESS_STRICT),
    ("strict", categories.STRICTNESS.STRICT),
    ("more-strict", categories.STRICTNESS.MORE_STRICT),
]

for strictness_name, strictness_value in strictness_levels:
    filter_content = textwrap.dedent(
        f"""
        # The following item filter was automatically generated.
        # This is a {strictness_name} filter.
        # Created on {datetime.datetime.now().strftime("%A %B %d %Y, %H:%M:%S")}.
        # Test at https://filterblast.xyz/advanced/Template
        """
    ).lstrip("\n")

    for rule in rules:
        if rule.strictness >= strictness_value:
            filter_content += str(rule)
        else:
            hide_rule = rule
            hide_rule.hide = True
            filter_content += str(hide_rule)

    FILTER_FILENAME = (
        "-".join([config.FILTER_NAME, strictness_name]) + "." + config.FILTER_EXTENSION
    )
    output_filepath = os.path.join(config.FILTER_OUTPUT_PATH, FILTER_FILENAME)
    with open(output_filepath, mode="w", encoding="utf-8") as output_file:
        output_file.write(filter_content)
        print(output_filepath)
