from enum import Enum
from operations.operation import Operation
from board import Board
from config import transparent_color
from config import number_of_colors
import element_groups

class ConnectionType(Enum):
    FourWayConnected = 1
    EightWayConnected = 2

class ColorSource(Enum):
    ParticularFromAllColors = 1
    FromGroup = 2
    FromElement = 3

class FillElements(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        
        any_change = False

        if args["ColorSource"] == ColorSource.ParticularFromAllColors:
            color = args["Color"]
        elif args["ColorSource"] == ColorSource.FromGroup:
            reference_group = args["Group"].get_element_group(board)
            if len(reference_group) == 0:
                return None
            color = reference_group[0].color
            if color is None:
                return None
        
        for element in elements:

            if args["ColorSource"] == ColorSource.FromElement:
                if element.color == None:
                    return None
                color = element.color

            if(element.height < 3 and element.width < 3):
                continue

            for i in range(1, element.height - 1):
                for j in range(1, element.width - 1):
                    if(element.matrix[i - 1][j] != transparent_color and
                       element.matrix[i][j - 1] != transparent_color and
                       element.matrix[i][j] == transparent_color):
                        if try_fill_area(element, j, i, color, args["ConnectionType"]) and not any_change:
                            any_change = True
        if any_change:
            return board
        return None


    @classmethod
    def gen_args(cls, board, elements):
        expected_colors = board.expected_result.colors
        for space_connection_type in ConnectionType:
            for color in expected_colors:
                yield {
                    "ColorSource": ColorSource.ParticularFromAllColors,
                    "Color": color , 
                    "ConnectionType": space_connection_type
                }
            for element_group_type in element_groups.ELEMENT_GROUPS:
                reference_group = element_group_type.get_element_group(board)
                if (len(reference_group) > 0 and
                reference_group[0].color != None and
                reference_group[0].color in expected_colors):
                    yield {
                        "ColorSource": ColorSource.FromGroup,
                        "Group": element_group_type , 
                        "ConnectionType": space_connection_type
                    }
            yield{
                    "ColorSource": ColorSource.FromElement,
                    "ConnectionType": space_connection_type
                }


def try_fill_area(element,
                  x, y,
                  color,
                  space_connection_type=ConnectionType.FourWayConnected):

    width = element.width
    height = element.height
    is_cell_checked = [[False] * width for i in range(height)]
    is_limited = [True]

    check_neighbours(y, x, is_limited, width, height,
                     is_cell_checked, element, space_connection_type)

    if not is_limited[0]:
        return False

    for i in range(height):
        for j in range(width):
            if is_cell_checked[i][j] == True:
                element.matrix[i][j] = color
    return True

def check_neighbours(y1, x1, is_limited, width, height,
                     is_cell_checked, element, space_connection_type):

    if not is_limited[0]:
        return

    if(y1 == 0 or
       y1 == height - 1 or
       x1 == 0 or
       x1 == width - 1):
        is_limited[0] = False
        return

    is_cell_checked[y1][x1] = True

    if(y1 > 0 and
       not is_cell_checked[y1 - 1][x1]
       and element.matrix[y1 - 1][x1] == transparent_color):
        check_neighbours(y1 - 1, x1, is_limited, width, height,
                         is_cell_checked, element, space_connection_type)
    if(y1 < height - 1 and
       not is_cell_checked[y1 + 1][x1]
       and element.matrix[y1 + 1][x1] == transparent_color):
        check_neighbours(y1 + 1, x1, is_limited, width, height,
                         is_cell_checked, element, space_connection_type)
    if(x1 > 0 and
       not is_cell_checked[y1][x1 - 1]
       and element.matrix[y1][x1 - 1] == transparent_color):
        check_neighbours(y1, x1 - 1, is_limited, width, height,
                         is_cell_checked, element, space_connection_type)
    if(x1 < width - 1 and
       not is_cell_checked[y1][x1 + 1]
       and element.matrix[y1][x1 + 1] == transparent_color):
        check_neighbours(y1, x1 + 1, is_limited, width, height,
                         is_cell_checked, element, space_connection_type)

    if space_connection_type == ConnectionType.EightWayConnected:
        if(y1 > 0 and
           x1 > 0 and
           not is_cell_checked[y1 - 1][x1 - 1]
           and element.matrix[y1 - 1][x1 - 1] == transparent_color):
            check_neighbours(y1 - 1, x1 - 1, is_limited, width, height,
                             is_cell_checked, element, space_connection_type)
        if(y1 > 0 and
           x1 < width - 1 and
           not is_cell_checked[y1 - 1][x1 + 1]
           and element.matrix[y1 - 1][x1 + 1] == transparent_color):
            check_neighbours(y1 - 1, x1 + 1, is_limited, width, height,
                             is_cell_checked, element, space_connection_type)
        if(y1 < height - 1 and
           x1 > 0 and
           not is_cell_checked[y1 + 1][x1 - 1]
           and element.matrix[y1 + 1][x1 - 1] == transparent_color):
            check_neighbours(y1 + 1, x1 - 1, is_limited, width, height,
                             is_cell_checked, element, space_connection_type)
        if(y1 < height - 1 and
           x1 < width - 1 and
           not is_cell_checked[y1 + 1][x1 + 1]
           and element.matrix[y1 + 1][x1 + 1] == transparent_color):
            check_neighbours(y1 + 1, x1 + 1, is_limited, width, height,
                             is_cell_checked, element, space_connection_type)
