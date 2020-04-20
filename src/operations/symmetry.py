from operations.operation import Operation
from board import Board
from enum import Enum


class SymmetryType(Enum):
    VERTICAL = 1
    HORIZONTAL = 2
    POINT = 3


class Symmetry(Operation):
    @classmethod
    def run_operation(cls, board: Board, args):
        for element in board.elements:
            elem_copy = [[value for value in row] for row in element.matrix]
            if args["symmetry_type"] == SymmetryType.HORIZONTAL:
                for i in range(len(elem_copy)):
                    for j in range(len(elem_copy[i])):
                        element.matrix[i][j] = \
                            elem_copy[len(elem_copy)-i-1][j]
            elif args["symmetry_type"] == SymmetryType.VERTICAL:
                for i in range(len(elem_copy)):
                    for j in range(len(elem_copy[i])):
                        element.matrix[i][j] = \
                            elem_copy[i][len(elem_copy[i])-j-1]
            elif args["symmetry_type"] == SymmetryType.POINT:
                for i in range(len(elem_copy)):
                    for j in range(len(elem_copy[i])):
                        element.matrix[i][j] = \
                            elem_copy[len(elem_copy)-i-1][len(elem_copy[i])-j-1]
        return board

    @classmethod
    def gen_args(cls, board):
        for symmetry_type in SymmetryType:
            yield {
                "symmetry_type": symmetry_type
            }
