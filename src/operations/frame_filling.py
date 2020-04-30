from operations.operation import Operation
from board import Board
from element import Element
from config import number_of_colors

class FrameFilling(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if board.height < 2 or board.width < 2:
            return None

        for element in elements:
            (begx, begy) = element.pos
            sizex = len(element.matrix[0])
            sizey = len(element.matrix)
            if begx == 0 or begy == 0 or begx + sizex == board.width - 1 or begy + sizey == board.height - 1:
                return None

        el1 = Element([[args for x in range(1)] for y in range((board.height - 1))], (0, 0), args)
        el2 = Element([[args for x in range(board.width - 1)] for y in range(1)], (board.height - 1, 0), args)
        el3 = Element([[args for x in range(1)] for y in range(board.height - 1)], (1, board.width - 1), args)
        el4 = Element([[args for x in range(board.width - 1)] for y in range(1)], (0, 1), args)

        board.elements.append(el1)
        board.elements.append(el2)
        board.elements.append(el3)
        board.elements.append(el4)

        board.element_group_counter.append(el1)
        board.element_group_counter.append(el2)
        board.element_group_counter.append(el3)
        board.element_group_counter.append(el4)

        return board

    @classmethod
    def gen_args(cls, board, elements):
        for i in range(number_of_colors):
            yield i
