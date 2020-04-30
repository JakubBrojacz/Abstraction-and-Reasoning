from .extract import Extract
from .connect_dots import ConnectDots
from .delete import Delete
from .move import Move
from .symmetry import Symmetry
from .filling_elements import FillElements
from .frame_filling import FrameFilling
from .mirror_reflection_of_board import MirrorReflectionOfBoard
from .shape_replication import ShapeReplication

OPERATIONS = [
    Extract,
    ConnectDots,
    Delete,
    MirrorReflectionOfBoard,
    Move,
    Symmetry,
    FillElements,
    FrameFilling,
    ShapeReplication
]
