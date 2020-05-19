from operations.operation import Operation
from board import Board
from operations.board_extension import BoardExtension
from operations.board_extension import ExtensionType
import config

class ShapeReplication(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if len(board.element_group_counter) != 0:
            return None

        b1 = board.copy()

        if args == True:
            width = board.width
            height = board.height

            if width * width > config.max_board_dimension_size:
                return None
            if height * height > config.max_board_dimension_size:
                return None

            extension = BoardExtension()

            board = extension.run_operation(board, elements, extension.create_arg(
                    ExtensionType.MULTIPLY, width, ExtensionType.MULTIPLY, height))
            
            elems = board.elements

        else:
            minx = board.width
            miny = board.height
            maxx = 0
            maxy = 0

            for element in elements:
                if element.width == 0 or element.height == 0:
                    continue
                minx = min(minx, element.pos[1])
                miny = min(miny, element.pos[0])
                maxx = max(maxx, element.pos[1] + element.width - 1)
                maxy = max(maxy, element.pos[0] + element.height - 1)

            width = maxx - minx + 1
            height = maxy - miny + 1

            if width * width > board.width or height * height > board.height:
                return None

            elems = []

            for element in elements:
                cloned = element.copy()
                cloned.pos = (cloned.pos[0] - miny, cloned.pos[1] - minx)
                elems.append(cloned)

        board.elements = []
        board.element_group = []
        board.element_group_counter = []

        where = [[False for i in range(width)] for j in range(height)]
        for element in elems:
            for y in range(element.height):
                for x in range(element.width):
                    if(element.matrix[y][x] == element.color):
                        where[y+element.pos[0]][x+element.pos[1]] = True

        for x in range(width):
            for y in range(height):
                if where[y][x] == True:
                    for element in elems:
                        newelement = element.copy()
                        newelement.pos = (newelement.pos[0] + y * height,
                                        newelement.pos[1] + x * width)
                        board.elements.append(newelement)
                        board.element_group.append(newelement)

        board.redraw()
        return board

    @classmethod
    def gen_args(cls, board, elements):
        yield True
        yield False
