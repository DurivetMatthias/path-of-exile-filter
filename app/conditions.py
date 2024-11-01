from app.extention import Extension
from app.categories import OPERATOR, RARITY


class AreaLevel(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.LTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            AreaLevel {self.operator} {self.value}
        """


class BaseArmour(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseArmour {self.operator} {self.value}
        """


class BaseDefensePercentile(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseDefencePercentile {self.operator} {self.value}
        """


class BaseEnergyShield(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseEnergyShield {self.operator} {self.value}
        """


class BaseEvasion(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseEvasion {self.operator} {self.value}
        """


class BaseType(Extension):
    def __init__(
        self,
        value: str,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseType {self.operator} "{self.value}"
        """


class Class(Extension):
    def __init__(
        self,
        value: str,
        operator: str = OPERATOR.EXACT,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Class {self.operator} "{self.value}"
        """


class Corrupted(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            Corrupted {self.value}
        """


class CorruptedMods(Extension):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            CorruptedMods {self.operator} {self.value}
        """


class ElderItem(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            ElderItem {self.value}
        """


class EnchantmentPassiveNum(Extension):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            EnchantmentPassiveNum {self.operator} {self.value}
        """


class FracturedItem(Extension):
    def __str__(self):
        return """
            FracturedItem true
        """


class GemLevel(Extension):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            GemLevel {self.operator} {self.value}
        """


class HasInfluence(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            HasInfluence {self.value}
        """


class Height(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Height {self.operator} {self.value}
        """


class Influenced(Extension):
    def __str__(self):
        return """
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


class ItemLevel(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            ItemLevel {self.operator} {self.value}
        """


class LinkedSockets(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            LinkedSockets {self.operator} {self.value}
        """


class MapTier(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            MapTier {self.operator} {self.value}
        """


class MultiBaseType(Extension):
    def __init__(
        self,
        values: list[str],
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        self.values = values
        self.operator = operator

    def __str__(self):
        if not self.values:
            raise ValueError("MultiBaseType got an empty list")
        base_types_string = " ".join(f'"{base_type}"' for base_type in self.values)
        return f"""
            BaseType {self.operator} {base_types_string}
        """


class MultiClass(Extension):
    def __init__(
        self,
        values: list[str],
        operator: OPERATOR = OPERATOR.EXACT,
    ):
        self.values = values
        self.operator = operator

    def __str__(self):
        if not self.values:
            raise ValueError("MultiClass got an empty list")
        class_names_string = " ".join(f'"{class_name}"' for class_name in self.values)
        return f"""
            Class {self.operator} {class_names_string}
        """


class Quality(Extension):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Quality {self.operator} {self.value}
        """


class Rarity(Extension):
    def __init__(
        self,
        value: RARITY,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Rarity {self.operator} {self.value}
        """


class Replica(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            Replica {self.value}
        """


class ShaperItem(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            ShaperItem {self.value}
        """


class SocketGroup(Extension):
    def __init__(
        self,
        value: str,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            SocketGroup {self.operator} {self.value}
        """


class Sockets(Extension):
    def __init__(
        self,
        value: str,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Sockets {self.operator} {self.value}
        """


class StackSize(Extension):
    def __init__(
        self,
        value: str,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            StackSize {self.operator} {self.value}
        """


class SynthesisedItem(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            SynthesisedItem {self.value}
        """


class TransfiguredGem(Extension):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            TransfiguredGem {self.value}
        """


class VeiledPrefix(Extension):
    def __str__(self):
        return """
            HasExplicitMod "Veiled"
        """


class VeiledSuffix(Extension):
    def __str__(self):
        return """
            HasExplicitMod "of the Veil"
        """


class Width(Extension):
    def __init__(
        self,
        value: str,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            Width {self.operator} {self.value}
        """
