from operations.operation import Operation
from board import Board

class LeaveDistinctElement(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if len(elements) <= 2:
            return None

        if elements[0].matrix == elements[1].matrix:
            template = elements[0].matrix
            distinct = -1
            start = 2
        else:
            start = 3
            if elements[0].matrix == elements[2].matrix:
                template = elements[0].matrix
                distinct = 1
            elif elements[1].matrix == elements[2].matrix:
                template = elements[1].matrix
                distinct = 0
            else:
                return None

        for i in range(start, len(elements)):
            if not elements[i].matrix == template:
                if distinct == -1:
                    distinct = i
                else:
                    return None

        if distinct == -1:
            return None

        board.elements = [elements[distinct].copy()]
        board.element_group = [board.elements[0].copy()]

        board.clean_matrix()
        board.draw_element(board.elements[0])
        for element in board.element_group_counter:
            board.draw_element(element)
            board.elements.append(element)

        return board

    @classmethod
    def gen_args(cls, board, elements):
        yield {}
