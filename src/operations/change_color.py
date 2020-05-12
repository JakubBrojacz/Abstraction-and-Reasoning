from enum import Enum
from operations.operation import Operation
from board import Board
from config import transparent_color
from config import number_of_colors
import element_groups

class ColorSource(Enum):
    ParticularFromAllColors = 1
    FromGroup = 2

class ChangeColor(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):

        if args["ColorSource"] == ColorSource.ParticularFromAllColors:
            color = args["Color"]
        elif args["ColorSource"] == ColorSource.FromGroup:
            reference_group = args["Group"].get_element_group(board)
            if len(reference_group) == 0:
                return None
            color = reference_group[0].color
            if color is None:
                return None

        for el in elements:
            for i in range(el.height):
                for j in range(el.width):
                    if el.matrix[i][j] != transparent_color:
                        el.matrix[i][j] = color

        return board


    @classmethod
    def gen_args(cls, board, elements):
        expected_colors = board.expected_result.colors
        for color in expected_colors: 
            yield {
                "ColorSource": ColorSource.ParticularFromAllColors,
                "Color": color
                }
        for element_group_type in element_groups.ELEMENT_GROUPS:
            reference_group = element_group_type.get_element_group(board)
            if (len(reference_group) > 0 and
                reference_group[0].color != None and
                reference_group[0].color in expected_colors):
                    yield {
                        "ColorSource": ColorSource.FromGroup,
                        "Group": element_group_type
                        }