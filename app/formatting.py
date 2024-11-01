import textwrap

from typing import Sequence

from app.extention import Extension
from app.blocks import Rule

TAB_WITH_SPACES = " " * 4


def format_header(header: str):
    return textwrap.dedent(header).strip("\n")


def format_extension(extension: Extension) -> str:
    return textwrap.dedent(str(extension)).strip("\n")


def format_extensions(extensions: Sequence[Extension]) -> str:
    extension_blocks = [format_extension(extension) for extension in extensions]
    return "\n".join(extension_blocks)


def format_rule(rule: Rule):
    instruction_text = format_extension(rule.instruction)
    extensions_text = format_extensions(rule.extensions)
    extensions_text = textwrap.indent(extensions_text, prefix=TAB_WITH_SPACES)
    return "\n".join([instruction_text, extensions_text])


def format_rules(rules: Sequence[Rule]):
    rule_blocks = [format_rule(rule) for rule in rules]
    return "\n\n".join(rule_blocks)


def format_filter(*, rules: list[Rule], header: str):
    rules_text = format_rules(rules)
    header_text = format_header(header)

    filter_text = "\n\n".join([header_text, rules_text])
    return filter_text
