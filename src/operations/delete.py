from operations.operation import Operation
from board import Board


class Delete(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        board.elements = [element for element in board.elements
                          if element not in elements]
        board.element_group = []
        return board

    @classmethod
    def gen_args(cls, board, elements):
        yield {}
