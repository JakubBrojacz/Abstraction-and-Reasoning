from operations.operation import Operation
from board import Board


class Move(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if validate_move(board, elements, args["x"], args["y"]):
            for element in elements:   
                    element.pos = (element.pos[0]+args["y"],
                                element.pos[1]+args["x"])
        else:
            return None
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
        if element.pos[1]+i < 0 or\
                element.pos[0] + j < 0 or\
                element.pos[0]+j+len(element.matrix) > board.height or\
                element.pos[1]+i+len(element.matrix[0]) > board.width:
            return False
    return True
