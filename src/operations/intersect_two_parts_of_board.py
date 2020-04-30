from operations.operation import Operation
from board import Board
from element import Element
from config import number_of_colors

class InterSectTwoPartsOfBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if board.width % 2 == 0:
            return None

        half_board_width = board.width/2;

        intersect_color = board.matrix[0][half_board_width]

        for i in range(board.height):
            if  board.matrix[i][half_board_width] != intersect_color:
                return None

        matrix = [
            [background_color for col in range(board.width/2)]
            for row in range(board.height)]
        new_board = board.Board(matrix)    

        for i in range(board.height):
            for j in range(board.width/2):
                if board.matrix[i][j] == board.matrix[i][second_half_board_width + j + 1]:
                    new_board.matrix[i][j] = 1

        return new_board

    @classmethod
    def gen_args(cls, board, elements):
        for i in range(number_of_colors):
            yield i

