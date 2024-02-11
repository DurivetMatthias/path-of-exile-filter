"""
This script fetches the divination card list from the community wiki.
It then outputs the names in a format that is easy to copy-paste
"""
import requests

from html.parser import HTMLParser


response = requests.get("https://www.poewiki.net/wiki/List_of_divination_cards")
html_response = response.text


class CardTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_table = False
        self.is_new_row = False
        self.is_card_span = False
        self.cards = []

    def handle_starttag(self, tag, _):
        if tag == "tbody":
            self.is_table = True
        if tag == "tr":
            self.is_new_row = True

        if self.is_table and tag == "a":
            self.is_card_span = True

    def handle_data(self, data):
        if self.is_table and self.is_card_span and self.is_new_row:
            self.cards.append(data)
            self.is_card_span = False
            self.is_new_row = False

    def handle_endtag(self, tag):
        if tag == "tbody":
            self.is_table = False


parser = CardTableParser()
parser.feed(html_response)

card_list = "\n".join([f'"{card}",' for card in parser.cards])

output_content = f"""
cards = [
    {card_list}
]
"""

OUTPUT_FILE_PATH = "./cards.py"
with open(OUTPUT_FILE_PATH, mode="w", encoding="utf-8") as output_file:
    output_file.write(output_content)
