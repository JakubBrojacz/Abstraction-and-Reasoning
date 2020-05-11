from operations.operation import Operation
from board import Board
from element import Element
from config import number_of_colors, background_color
from enum import Enum


class OperationType(Enum):
    OR = 1
    NOR = 2
    XOR = 3


class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class InterSectTwoPartsOfBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        half_board_width = int(board.width/2)
        half_board_height = int(board.height/2)

        if len(board.element_group) != len(board.elements):
            return None

        if args["direction"] == Direction.VERTICAL:
            matrix = [
                [1 for col in range(half_board_width)]
                for row in range(board.height)]

            if args["operation_type"] == OperationType.OR:
                matrix = [[value for value in row] for row in or_operation_vertically(
                    board, matrix, half_board_width)]
            if args["operation_type"] == OperationType.NOR:
                matrix = [[value for value in row] for row in or_operation_vertically(
                    board, matrix, half_board_width)]
                matrix = [[(0, 1)[value == 0] for value in row]
                          for row in matrix]
            if args["operation_type"] == OperationType.XOR:
                matrix = [[value for value in row] for row in xor_operation_vertically(
                    board, matrix, half_board_width)]

            board.matrix = [
                [background_color for col in range(half_board_width)]
                for row in range(board.height)]
            board.elements = []
            board.element_group = []
            board.element_group_counter = []

            for i in range(board.height):
                for j in range(half_board_width):
                    if matrix[i][j] == 1:
                        el = Element([[args["color"] for x in range(1)]
                                      for y in range(1)], (i, j), args["color"])
                        board.elements.append(el)
                        board.element_group_counter.append(el)

        elif args["direction"] == Direction.HORIZONTAL:
            matrix = [
                [1 for col in range(board.width)]
                for row in range(half_board_height)]

            if args["operation_type"] == OperationType.OR:
                matrix = [[value for value in row] for row in or_operation_horizontally(
                    board, matrix, half_board_height)]
            if args["operation_type"] == OperationType.NOR:
                matrix = [[value for value in row] for row in or_operation_horizontally(
                    board, matrix, half_board_height)]
                matrix = [[(0, 1)[value == 0] for value in row]
                          for row in matrix]
            if args["operation_type"] == OperationType.XOR:
                matrix = [[value for value in row] for row in xor_operation_horizontally(
                    board, matrix, half_board_height)]

            board.matrix = [
                [background_color for col in range(board.width)]
                for row in range(half_board_height)]
            board.elements = []
            board.element_group = []
            board.element_group_counter = []

            for i in range(half_board_height):
                for j in range(board.width):
                    if matrix[i][j] == 1:
                        el = Element([[args["color"] for x in range(1)]
                                      for y in range(1)], (i, j), args["color"])
                        board.elements.append(el)
                        board.element_group_counter.append(el)
        else:
            return None

        return board

    @classmethod
    def gen_args(cls, board, elements):
        h_divided, col_h = is_horizontally_divided(board)
        v_divided, col_v = is_vertically_divided(board)
        col_result_h, col_result_v = get_colors_from_result(board, col_v,
                                                            col_h)
        for operation_type in OperationType:
            if h_divided and col_result_h is not None:
                yield {
                    "operation_type": operation_type,
                    "color": col_result_h,
                    "direction": Direction.HORIZONTAL
                }
            if v_divided and col_result_v is not None:
                yield {
                    "operation_type": operation_type,
                    "color": col_result_v,
                    "direction": Direction.VERTICAL
                }


def is_horizontally_divided(board):
    if board.height % 2 == 0:
        return False, -1

    half_board_height = int(board.height/2)

    intersect_color = board.matrix[half_board_height][0]

    for i in range(board.width):
        if board.matrix[half_board_height][i] != intersect_color:
            return False, -1

    return True, intersect_color


def is_vertically_divided(board):
    if board.width % 2 == 0:
        return False, -1

    half_board_width = int(board.width/2)

    intersect_color = board.matrix[0][half_board_width]

    for i in range(board.height):
        if board.matrix[i][half_board_width] != intersect_color:
            return False, -1

    return True, intersect_color


def get_colors_from_result(board, col_v, col_h):
    matrix = board.expected_result.matrix
    col_result_v = None
    col_result_h = None
    for i in range(board.expected_result.height):
        for j in range(board.expected_result.width):
            if matrix[i][j] != background_color:
                if col_result_v is None and matrix[i][j] != col_v:
                    col_result_v = matrix[i][j]
                if col_result_h is None and matrix[i][j] != col_h:
                    col_result_h = matrix[i][j]
                if col_result_v is None and col_result_h is None:
                    return col_result_h, col_result_v
    return col_result_h, col_result_v


def or_operation_vertically(board, matrix, half_board_width):
    for i in range(board.height):
        for j in range(half_board_width):
            if board.matrix[i][j] == board.matrix[i][half_board_width + j + 1] and board.matrix[i][j] == background_color:
                matrix[i][j] = 0
    return matrix


def or_operation_horizontally(board, matrix, half_board_height):
    for i in range(half_board_height):
        for j in range(board.width):
            if board.matrix[i][j] == board.matrix[half_board_height + i + 1][j] and board.matrix[i][j] == background_color:
                matrix[i][j] = 0
    return matrix


def xor_operation_vertically(board, matrix, half_board_width):
    for i in range(board.height):
        for j in range(half_board_width):
            if (board.matrix[i][j] == background_color and board.matrix[i][half_board_width + j + 1] == background_color) or (board.matrix[i][j] != background_color and board.matrix[i][half_board_width + j + 1] != background_color):
                matrix[i][j] = 0
    return matrix


def xor_operation_horizontally(board, matrix, half_board_height):
    for i in range(half_board_height):
        for j in range(board.width):
            if (board.matrix[i][j] == background_color and board.matrix[half_board_height + i + 1][j] == background_color) or (board.matrix[i][j] != background_color and board.matrix[half_board_height + i + 1][j] != background_color):
                matrix[i][j] = 0
    return matrix
