from enum import Enum
from operations.operation import Operation
from board import Board
import config

class ExtensionType(Enum):
    UNITS = 1
    MULTIPLY = 2


class BoardExtension(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        (xtype, xarg) = args["x"]
        (ytype, yarg) = args["y"]

        if xtype == ExtensionType.UNITS:
            xsize = board.width + xarg
        elif xtype == ExtensionType.MULTIPLY:
            xsize = board.width * xarg

        if ytype == ExtensionType.UNITS:
            ysize = board.height + yarg
        elif ytype == ExtensionType.MULTIPLY:
            ysize = board.height * yarg

        if xsize > config.max_board_dimension_size or ysize > config.max_board_dimension_size:
            return None
  
        board.matrix = [[0 for x in range(xsize)] for y in range(ysize)]
        for element in board.elements:
            board.draw_element(element)

        return board

    @classmethod
    def gen_args(cls, board, elements):
        xsize = board.width
        ysize = board.height
        for x_extension_type in ExtensionType:
            for y_extension_type in ExtensionType:
                if x_extension_type == ExtensionType.UNITS:
                    xdelta = 1
                elif x_extension_type == ExtensionType.MULTIPLY:
                    xdelta = xsize

                if y_extension_type == ExtensionType.UNITS:
                    ydelta = 1
                elif y_extension_type == ExtensionType.MULTIPLY:
                    ydelta = ysize

                xarg = 1
                xnext = xsize + xdelta

                while xnext <= config.max_board_dimension_size:
                    yarg = 1
                    ynext = ysize + ydelta
                    while ynext <= config.max_board_dimension_size:
                        yield cls.create_arg(x_extension_type, xarg, y_extension_type, yarg)
                        ynext += ydelta
                        yarg += 1
                    xnext += xdelta
                    xarg += 1

    @classmethod
    def create_arg(self, xtype, xarg, ytype, yarg):
        return {
            "x": (xtype, xarg),
            "y": (ytype, yarg)
        }
