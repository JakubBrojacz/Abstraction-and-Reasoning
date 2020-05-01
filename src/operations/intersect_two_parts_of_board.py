from operations.operation import Operation
from board import Board
from element import Element
from config import number_of_colors

class InterSectTwoPartsOfBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        half_board_width = board.width/2;
        half_board_height = board.height/2;

        if is_vertically_divided(board):
            matrix = [
                [background_color for col in range(half_board_width)]
                for row in range(board.height)]
            new_board = board.Board(matrix)    

            for i in range(board.height):
                for j in range(half_board_width):
                    if board.matrix[i][j] == board.matrix[i][half_board_width + j + 1]:
                        new_board.matrix[i][j] = 1
        elif is_horizontally_divided(board):
            matrix = [
                [background_color for col in range(board.width)]
                for row in range(half_board_height)]
            new_board = board.Board(matrix)    

            for i in range(half_board_height):
                for j in range(board.width):
                    if board.matrix[i][j] == board.matrix[half_board_height + i + 1][j]:
                        new_board.matrix[i][j] = 1
        else:
            return None

        return new_board

    @classmethod
    def gen_args(cls, board, elements):
        for i in range(number_of_colors):
            yield i


def is_horizontally_divided(board):
    if board.height % 2 == 0:
        return False

    half_board_height = board.height/2;

    intersect_color = board.matrix[half_board_height][0]

    for i in range(board.width):
        if  board.matrix[half_board_height][i] != intersect_color:
            return False

    return True


def is_vertically_divided(board):
    if board.width % 2 == 0:
        return False

    half_board_width = board.width/2;

    intersect_color = board.matrix[0][half_board_width]

    for i in range(board.height):
        if  board.matrix[i][half_board_width] != intersect_color:
            return False

    return True