from operations.operation import Operation
from board import Board


class Extract(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if len(elements) != 1:
            return None
        if (elements[0].height == board.height and
            elements[0].width == board.width):
            return None
        board.matrix = [
            [color for color in row]
            for row in elements[0].matrix]
        elements[0].pos = (0, 0)
        board.elements = [elements[0].copy()]
        board.element_group = [elements[0].copy()]
        board.element_group_counter = []
        return board

    @classmethod
    def gen_args(cls, board, elements):
        yield {}
