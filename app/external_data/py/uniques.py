import csv
import dataclasses
import os


@dataclasses.dataclass
class Unique:
    name: str
    base_type: str
    item_class: str
    tier: int
    method: str
    poedb: str
    poewiki: str


field_to_column = {
    "name": "name",
    "base_type": "baseItem",
    "item_class": "category",
    "tier": "tier",
    "method": "grouping",
    "poedb": "poedbUrl",
    "poewiki": "poewikilink",
}

uniques = []

with open(
    os.path.join("app", "external_data", "csv", "3.23", "poeladder_uniques.csv")
) as all_uniques_csv:
    lines = list(csv.reader(all_uniques_csv))
    header = lines.pop(0)
    column_to_index = {}

    for index, column in enumerate(header):
        column_to_index[column] = index

    def get_field(field, line):
        column = field_to_column[field]
        index = column_to_index[column]
        return line[index]

    for line in lines:
        uniques.append(
            Unique(
                name=get_field("name", line),
                base_type=get_field("base_type", line),
                item_class=get_field("item_class", line),
                tier=get_field("tier", line),
                method=get_field("method", line),
                poedb=get_field("poedb", line),
                poewiki=get_field("poewiki", line),
            )
        )
