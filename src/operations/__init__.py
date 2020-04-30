from .move import Move
from .symmetry import Symmetry
from .filling_elements import FillElements
from .mirror_reflection_of_board import MirrorReflectionOfBoard

OPERATIONS = [
    MirrorReflectionOfBoard,
    Move,
    Symmetry,
    FillElements
]
