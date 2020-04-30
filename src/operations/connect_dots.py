from operations.operation import Operation
from board import Board
from config import background_color
from element import Element
from enum import Enum


class ConnectionType(Enum):
    HORIZONTAL_ON_TOP = 1
    VERTICAL_ON_TOP = 2
    DIAGONAL = 3
    RECTANGLE = 4


class ConnectDots(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        max_color = -1
        for element in elements:
            if element.matrix[0][0] > max_color:
                max_color = element.matrix[0][0]
            if len(element.matrix) != 1 or len(element.matrix[0]) != 1:
                return None
        if max_color == -1:
            return None
        new_elements = [element.copy() for element
                        in board.element_group_counter]
        new_elements_group = []
        for color in range(max_color + 1):
            elements_in_color = []
            for element in elements:
                if element.matrix[0][0] == color:
                    elements_in_color.append(element)
            if len(elements_in_color) != 2:
                new_elements.extend([element.copy() for element
                                     in elements_in_color])
                new_elements_group.extend([element.copy() for element
                                           in elements_in_color])
                continue
            min_pos_0 = min(elements_in_color[0].pos[0],
                            elements_in_color[1].pos[0])
            max_pos_0 = max(elements_in_color[0].pos[0],
                            elements_in_color[1].pos[0])
            min_pos_1 = min(elements_in_color[0].pos[1],
                            elements_in_color[1].pos[1])
            max_pos_1 = max(elements_in_color[0].pos[1],
                            elements_in_color[1].pos[1])
            if (min_pos_0 != max_pos_0 and min_pos_1 != max_pos_1 and
                (args["connection_type"] ==
                 ConnectionType.HORIZONTAL_ON_TOP or
                 args["connection_type"] ==
                 ConnectionType.VERTICAL_ON_TOP)) or\
                (max_pos_0 - min_pos_0 != max_pos_1 - min_pos_1 and
                 args["connection_type"] == ConnectionType.DIAGONAL):
                new_elements.extend([element.copy() for element
                                     in elements_in_color])
                new_elements_group.extend([element.copy() for element
                                           in elements_in_color])
                continue
            if args["connection_type"] == ConnectionType.DIAGONAL:
                new_matrix = [
                    [background_color] * (max_pos_1 - min_pos_1 + 1)
                    for k in range(max_pos_0 - min_pos_0 + 1)]
                if elements_in_color[0].pos[0] == min_pos_0 and\
                        elements_in_color[0].pos[1] == min_pos_1:
                    for i in range(max_pos_0 - min_pos_0 + 1):
                        new_matrix[i][i] = color
                else:
                    for i in range(max_pos_0 - min_pos_0 + 1):
                        new_matrix[max_pos_0 - min_pos_0 - i][i] = color
            else:
                new_matrix = [
                    [color] * (max_pos_1 - min_pos_1 + 1)
                    for k in range(max_pos_0 - min_pos_0 + 1)]
            new_element = Element(new_matrix,
                                  (min(elements_in_color[0].pos[0],
                                       elements_in_color[1].pos[0]),
                                   min(elements_in_color[0].pos[1],
                                       elements_in_color[1].pos[1])),
                                  color)
            if (args["connection_type"] ==
                    ConnectionType.HORIZONTAL_ON_TOP and
                    min_pos_1 == max_pos_1) or\
                    (args["connection_type"] ==
                        ConnectionType.VERTICAL_ON_TOP and
                        min_pos_0 == max_pos_0):
                new_elements.insert(0, new_element.copy())
                new_elements_group.insert(0, new_element.copy())
            else:
                new_elements.append(new_element.copy())
                new_elements_group.append(new_element.copy())
        board.elements = new_elements
        board.element_group = new_elements_group
        return board

    @classmethod
    def gen_args(cls, board, elements):
        for connection_type in ConnectionType:
            yield {
                "connection_type": connection_type
            }
