from enum import StrEnum, auto


class TypeOfTests(StrEnum):
    """An enumeration class representing different types of tests"""

    LIST_CREATION = auto()
    STRING_CONCATENATION = auto()
    DATA_SERIALIZATION = auto()
