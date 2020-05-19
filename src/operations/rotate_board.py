from operations.operation import Operation
from board import Board
from config import background_color

class RotateBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        matrix = board.matrix
        if args == 90:
            matrix = rotate_matrix_90(matrix)
        if args == 180:
            matrix = rotate_matrix_180(matrix)
        if args == 270:
            matrix = rotate_matrix_270(matrix)

        board.matrix = matrix
        board.set_split_type(board.split_type)
        board.set_element_group_type(board.element_group_type)

        return board

    @classmethod
    def gen_args(cls, board, elements):
        for i in [90, 180, 270]:
            yield i


def rotate_matrix_90(matrix):
    width = len(matrix)
    if width == 0:
        return matrix
    height = len(matrix[0])
    new_matrix = [[background_color for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            new_matrix[y][x] = matrix[x][height - y - 1]
    return new_matrix


def rotate_matrix_180(matrix):
    height = len(matrix)
    if height == 0:
        return matrix
    width = len(matrix[0])
    new_matrix = [[background_color for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            new_matrix[y][x] = matrix[height - y - 1][width - x - 1]
    return new_matrix


def rotate_matrix_270(matrix):
    width = len(matrix)
    if width == 0:
        return matrix
    height = len(matrix[0])
    new_matrix = [[background_color for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            new_matrix[y][x] = matrix[width - x - 1][y]
    return new_matrix
