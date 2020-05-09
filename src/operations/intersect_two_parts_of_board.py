from operations.operation import Operation
from board import Board
from element import Element
from config import number_of_colors, background_color

class InterSectTwoPartsOfBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        half_board_width = int(board.width/2);
        half_board_height = int(board.height/2);

        if len(board.element_group) != len(board.elements):
            return None;

        if is_vertically_divided(board):
            matrix = [
                [1 for col in range(half_board_width)]
                for row in range(board.height)]

            for i in range(board.height):
                for j in range(half_board_width):
                    if board.matrix[i][j] == board.matrix[i][half_board_width + j + 1] and board.matrix[i][j] == background_color:
                        matrix[i][j] = 0

            board.matrix = [
                [background_color for col in range(half_board_width)]
                for row in range(board.height)]
            board.elements = []
            board.element_group = []
            board.element_group_counter = []

            for i in range(board.height):
                for j in range(half_board_width):
                    if matrix[i][j] == 1:
                        el = Element([[args for x in range(1)] for y in range(1)], (i, j), args)
                        board.elements.append(el)
                        board.element_group_counter.append(el)

        elif is_horizontally_divided(board):
            matrix = [
                [1 for col in range(board.width)]
                for row in range(half_board_height)]

            for i in range(half_board_height):
                for j in range(board.width):
                    if board.matrix[i][j] == board.matrix[half_board_height + i + 1][j] and board.matrix[i][j] == background_color:
                        matrix[i][j] = 0

            board.matrix = [
                [background_color for col in range(board.width)]
                for row in range(half_board_height)]
            board.elements = []
            board.element_group = []
            board.element_group_counter = []

            for i in range(half_board_height):
                for j in range(board.width):
                    if matrix[i][j] == 1:
                        el = Element([[args for x in range(1)] for y in range(1)], (i, j), args)
                        board.elements.append(el)
                        board.element_group_counter.append(el)
        else:
            return None

        return board

    @classmethod
    def gen_args(cls, board, elements):
        for i in range(number_of_colors):
            yield i


def is_horizontally_divided(board):
    if board.height % 2 == 0:
        return False

    half_board_height = int(board.height/2);

    intersect_color = board.matrix[half_board_height][0]

    for i in range(board.width):
        if  board.matrix[half_board_height][i] != intersect_color:
            return False

    return True


def is_vertically_divided(board):
    if board.width % 2 == 0:
        return False

    half_board_width = int(board.width/2);

    intersect_color = board.matrix[0][half_board_width]

    for i in range(board.height):
        if  board.matrix[i][half_board_width] != intersect_color:
            return False

    return True