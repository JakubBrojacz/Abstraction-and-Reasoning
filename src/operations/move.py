from operations.operation import Operation
from board import Board


class Move(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        for element in elements:
            element.pos = (element.pos[0]+args["x"],
                           element.pos[1]+args["y"])
        return board

    @classmethod
    def gen_args(cls, board, elements):
        # for i in range(-board.height, board.height):
        #     for j in range(-board.width, board.width):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if validate_move(board, elements, i, j):
                    yield {
                        "x": i,
                        "y": j
                    }


def validate_move(board, elements, i, j):
    for element in elements:
        if element.pos[0]+i < 0 or\
                element.pos[1] + j < 0 or\
                element.pos[0]+i+len(element.matrix) > board.height or\
                element.pos[1]+j+len(element.matrix[0]) > board.width:
            return False
    return True
