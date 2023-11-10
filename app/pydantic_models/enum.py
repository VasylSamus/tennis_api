from enum import Enum


def to_dict(enum):
    return {item.name: item.value for item in enum}


class HandEnum(Enum):
    __order__ = "LEFT RIGHT"
    LEFT: str = "left"
    RIGHT: str = "right"


class BackhandTypeEnum(Enum):
    __order__ = "ONE_HAND TWO_HAND"
    ONE_HAND: str = "one hand"
    TWO_HAND: str = "two hand"


class MatchTypeEnum(Enum):
    __order__ = "SINGLE DOUBLE MIXED"
    SINGLE: str = "single"
    DOUBLE: str = "double"
    MIXED: str = "mixed"


class GenderEnum(Enum):
    __order__ = "MALE FEMALE"
    MALE: str = "male"
    FEMALE: str = "female"


class SurfaceTypeEnum(Enum):
    __order__ = "CLAY GRASS HARD CARPET SYNTHETIC_GRASS"
    CLAY: str = "clay"
    GRASS: str = "grass"
    HARD: str = "hard court"
    CARPET: str = "carpet"
    SYNTHETIC_GRASS: str = "synthetic grass"


class TournamentStageTypeEnum(Enum):
    __order__ = "GROUP PLAYOFF"
    GROUP: str = "group"
    PLAYOFF: str = "playoff"
