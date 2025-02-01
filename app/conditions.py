from app.categories import OPERATOR, RARITY


class Condition:
    def __str__(self):
        raise NotImplementedError


class AreaLevel(Condition):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            AreaLevel {self.operator} {self.value}
        """


class BaseArmour(Condition):
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


class BaseDefensePercentile(Condition):
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


class BaseEnergyShield(Condition):
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


class BaseEvasion(Condition):
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


class BaseType(Condition):
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


class Class(Condition):
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


class Corrupted(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            Corrupted {self.value}
        """


class CorruptedMods(Condition):
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


class ElderItem(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            ElderItem {self.value}
        """


class EnchantmentPassiveNum(Condition):
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


class FracturedItem(Condition):
    def __str__(self):
        return """
            FracturedItem true
        """


class GemLevel(Condition):
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


class HasInfluence(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            HasInfluence {self.value}
        """


class Height(Condition):
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


class Influenced(Condition):
    def __str__(self):
        return """
            HasInfluence "Shaper" "Elder" "Crusader" "Hunter" "Redeemer" "Warlord"
        """


class ItemLevel(Condition):
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


class LinkedSockets(Condition):
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


class MapTier(Condition):
    def __init__(
        self,
        value: int,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            WaystoneTier {self.operator} {self.value}
        """


class MultiBaseType(Condition):
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


class MultiClass(Condition):
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


class Quality(Condition):
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


class Rarity(Condition):
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


class Replica(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            Replica {self.value}
        """


class ShaperItem(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            ShaperItem {self.value}
        """


class SocketGroup(Condition):
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


class Sockets(Condition):
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


class StackSize(Condition):
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


class SynthesisedItem(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            SynthesisedItem {self.value}
        """


class TransfiguredGem(Condition):
    def __init__(
        self,
        value: bool,
    ):
        self.value = value

    def __str__(self):
        return f"""
            TransfiguredGem {self.value}
        """


class VeiledPrefix(Condition):
    def __str__(self):
        return """
            HasExplicitMod "Veiled"
        """


class VeiledSuffix(Condition):
    def __str__(self):
        return """
            HasExplicitMod "of the Veil"
        """


class Width(Condition):
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
