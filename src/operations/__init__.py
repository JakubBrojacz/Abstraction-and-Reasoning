from .extract import Extract
from .connect_dots import ConnectDots
from .delete import Delete
from .move import Move
from .symmetry import Symmetry
from .filling_elements import FillElements
from .board_extension import BoardExtension
from .mirror_reflection_of_board import MirrorReflectionOfBoard

OPERATIONS = [
    Extract,
    ConnectDots,
    Delete,
    MirrorReflectionOfBoard,
    Move,
    Symmetry,
    FillElements,
    BoardExtension
]
