from .connect_dots import ConnectDots
from .delete import Delete
from .move import Move
from .symmetry import Symmetry
from .filling_elements import FillElements
from .mirror_reflection_of_board import MirrorReflectionOfBoard

OPERATIONS = [
    ConnectDots,
    Delete,
    MirrorReflectionOfBoard,
    Move,
    Symmetry,
    FillElements
]
