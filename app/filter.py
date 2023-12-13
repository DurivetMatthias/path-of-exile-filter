"""
Programmatically generate item filter files.
This project aims to simplify the configuration of colors, sounds, effects etc.
This is done by adding tags to all items and then applying rules to those tags.
In doing so we avoid the many to many assignment of properties and try to
reduce it to one-to-one as much as possible
"""
import os
import datetime

from app import formatting

FILTER_EXTENSION = "filter"
FILTER_OUTPUT_PATH = "C:\\Users\\matth\\Documents\\my games\\Path of Exile"


def generate(*, rules, filter_name):
    header = f"""
        # The following item filter was automatically generated.
        # Created on {datetime.datetime.now().strftime("%A %B %d %Y, %H:%M:%S")}.
    """
    file_content = formatting.format_filter(
        rules=rules,
        header=header,
    )

    filter_filename = f"{filter_name}.{FILTER_EXTENSION}"
    output_filepath = os.path.join(FILTER_OUTPUT_PATH, filter_filename)
    with open(output_filepath, mode="w", encoding="utf-8") as output_file:
        output_file.write(file_content)
    print("==============")
    print("Inspect the item filter:")
    print(output_filepath)
    print("==============")
