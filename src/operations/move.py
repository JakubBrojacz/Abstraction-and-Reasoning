from operations.operation import Operation
from board import Board


class Move(Operation):
    @classmethod
    def run_operation(cls, board: Board, args):
        element = board.elements[args["element"]]
        element.pos = (element.pos[0]+args["x"],
                       element.pos[1]+args["y"])
        return board

    @classmethod
    def gen_args(cls, board):
        for element in range(len(board.elements)):
            # for i in range(-board.height, board.height):
            #     for j in range(-board.width, board.width):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if validate_move(board, board.elements[element], i, j):
                        yield {
                            "x": i,
                            "y": j,
                            "element": element
                        }


def validate_move(board, element, i, j):
    if element.pos[0]+i >= 0 and\
            element.pos[1] + j >= 0 and\
            element.pos[0]+i+len(element.matrix) < board.height and\
            element.pos[1]+j+len(element.matrix[0]) < board.width:
        return True
    return False
