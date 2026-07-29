from app.categories import *


class Condition:
    def __str__(self):
        raise NotImplementedError


class AreaLevel(Condition):
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


class BaseArmour(Condition):
    def __init__(
        self,
        value: int = 1,
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
        value: int = 1,
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
        value: int = 1,
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
        operator: OPERATOR = OPERATOR.EXACT,
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
        values: list,
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
        values: list,
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
        value: int = 1,
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
        operator: OPERATOR = OPERATOR.EXACT,
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
        value: int,
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
        value: int,
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


class UnidentifiedItemTier(Condition):
    def __init__(
        self,
        value: int = 2,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            UnidentifiedItemTier  {self.operator} {self.value}
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


class PureArmour(Condition):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseArmour {self.operator} {self.value}
            BaseEvasion == 0
            BaseEnergyShield == 0
        """


class PureEvasion(Condition):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseArmour == 0
            BaseEvasion {self.operator} {self.value}
            BaseEnergyShield == 0
        """


class PureEnergyShield(Condition):
    def __init__(
        self,
        value: int = 1,
        operator: OPERATOR = OPERATOR.GTE,
    ):
        self.value = value
        self.operator = operator

    def __str__(self):
        return f"""
            BaseArmour == 0
            BaseEvasion == 0
            BaseEnergyShield {self.operator} {self.value}
        """


class HybridArmourEvasion(Condition):
    def __str__(self):
        return """
            BaseArmour >= 1
            BaseEvasion >= 1
            BaseEnergyShield == 0
        """


class HybridArmourEnergyShield(Condition):
    def __str__(self):
        return """
            BaseArmour >= 1
            BaseEvasion == 0
            BaseEnergyShield >= 1
        """


class HybridEvasionEnergyShield(Condition):
    def __str__(self):
        return """
            BaseArmour == 0
            BaseEvasion >= 1
            BaseEnergyShield >= 1
        """


class ArmourAndHybrid(Condition):
    def __str__(self):
        return """
            BaseArmour >= 1
        """


class EnergyShieldAndHybrid(Condition):
    def __str__(self):
        return """
            BaseEnergyShield >= 1
        """


class EvasionAndHybrid(Condition):
    def __str__(self):
        return """
            BaseEvasion >= 1
        """


class HasVaalUniqueMod(Condition):
    def __init__(
        self,
        value: bool = True,
    ):
        self.value = value

    def __str__(self):
        return f"""
            HasVaalUniqueMod {self.value}
        """


class TwiceCorrupted(Condition):
    def __init__(
        self,
        value: bool = True,
    ):
        self.value = value

    def __str__(self):
        return f"""
            TwiceCorrupted {self.value}
        """


class IsVaalUnique(Condition):
    def __init__(
        self,
        value: bool = True,
    ):
        self.value = value

    def __str__(self):
        return f"""
            IsVaalUnique {self.value}
        """


class NullCondition(Condition):
    def __str__(self):
        return ""


class GearClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(["Body Armours", "Helmets", "Gloves", "Boots"])

    def __str__(self):
        return str(self.condition)


class JewelryClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(["Rings", "Amulets", "Belts"])

    def __str__(self):
        return str(self.condition)


class WeaponClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(
            [
                "Bows",
                "Claws",
                "Traps",
                "Wands",
                "Flails",
                "Staves",
                "Spears",
                "Daggers",
                "Sceptres",
                "Crossbows",
                "Talismans",
                "Fishing Rods",
                "One Hand Axes",
                "Two Hand Axes",
                "Quarterstaves",
                "One Hand Maces",
                "Two Hand Maces",
                "One Hand Swords",
                "Two Hand Swords",
            ]
        )

    def __str__(self):
        return str(self.condition)


class OneHandedWeaponClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(
            [
                "Wands",
                "Spears",
                "Sceptres",
                "Fishing Rods",
                "One Hand Axes",
                "One Hand Maces",
                "One Hand Swords",
            ]
        )

    def __str__(self):
        return str(self.condition)


class TwoHandedWeaponClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(
            [
                "Bows",
                "Staves",
                "Crossbows",
                "Talismans",
                "Fishing Rods",
                "Quarterstaves",
                "Two Hand Axes",
                "Two Hand Maces",
                "Two Hand Swords",
            ]
        )

    def __str__(self):
        return str(self.condition)


class OffhandClasses(Condition):
    def __init__(self):
        self.condition = MultiClass(
            [
                "Foci",
                "Quivers",
                "Shields",
                "Bucklers",
            ]
        )

    def __str__(self):
        return str(self.condition)
