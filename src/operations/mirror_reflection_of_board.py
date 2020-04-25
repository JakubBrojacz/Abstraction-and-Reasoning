import board
from operations.operation import Operation
from board import Board
from enum import Enum
from config import background_color
import element_groups

class ReflectionType(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class MirrorReflectionOfBoard(Operation):
    @classmethod
    def run_operation(cls, board: Board, elements, args):
        if args["referenced_to_group"] == False:
            if args["reflection_type"] == ReflectionType.UP:
                return up_reflection(board)
            elif args["reflection_type"] == ReflectionType.DOWN:
                return down_reflection(board)
            elif args["reflection_type"] == ReflectionType.RIGHT:
                return right_reflection(board)
            elif args["reflection_type"] == ReflectionType.LEFT:
                return left_reflection(board)

        return None


    @classmethod
    def gen_args(cls, board, elements):
        for reflection_type in ReflectionType:
            yield {
                "referenced_to_group" : False,
                "reflection_type": reflection_type
            }
        for element_group_type in element_groups.ELEMENT_GROUPS:
            yield{
                    "referenced_to_group" : True,
                    "group" : element_group_type
                }


def up_reflection(old_board):                
    matrix = [
        [background_color for element in range(old_board.width)]
        for row in range(2 * old_board.height)]
    new_board = board.Board(matrix)
    elements1 = [element.copy() for element in old_board.elements]
    for element in elements1:
        element.pos = (element.pos[0]+ old_board.height , element.pos[1])
    elements2 = [element.copy() for element in old_board.elements]
    for element in elements2:
        element.pos = (old_board.height - element.pos[0] - len(element.matrix), element.pos[1])
        element = horizontal_symmetry(element)
    add_elements_to_new_board(old_board, new_board, elements1, elements2)
    return new_board

def down_reflection(old_board):                
    matrix = [
        [background_color for element in range(old_board.width)]
        for row in range(2 * old_board.height)]
    new_board = board.Board(matrix)
    elements1 =[element.copy() for element in old_board.elements]
    elements2 = [element.copy() for element in old_board.elements]
    for element in elements2:
        element.pos = (2 * old_board.height - element.pos[0] - len(element.matrix), element.pos[1])
        element = horizontal_symmetry(element)
    add_elements_to_new_board(old_board, new_board, elements1, elements2)
    return new_board

def right_reflection(old_board):                
    matrix = [
        [background_color for element in range(2*old_board.width)]
        for row in range(old_board.height)]
    new_board = board.Board(matrix)
    elements1 =[element.copy() for element in old_board.elements]
    elements2 = [element.copy() for element in old_board.elements]
    for element in elements2:
        element.pos = (element.pos[0], 2 * old_board.width - element.pos[1] - len(element.matrix[0]))
        element = vertical_symmetry(element)
    add_elements_to_new_board(old_board, new_board, elements1, elements2)
    return new_board

def left_reflection(old_board):                
    matrix = [
        [background_color for element in range(2 * old_board.width)]
        for row in range(old_board.height)]
    new_board = board.Board(matrix)
    elements1 = [element.copy() for element in old_board.elements]
    for element in elements1:
        element.pos = (element.pos[0], element.pos[1] + old_board.width)
    elements2 = [element.copy() for element in old_board.elements]
    for element in elements2:
        element.pos = (element.pos[0], old_board.width - element.pos[1] - len(element.matrix[0]))
        element = vertical_symmetry(element)
    add_elements_to_new_board(old_board, new_board, elements1, elements2)
    return new_board

def add_elements_to_new_board(old_board, new_board, elements1, elements2):
    new_board.elements = elements1
    new_board.elements.extend(elements2)
    for element in new_board.elements:
        new_board.draw_element(element)
    new_board.set_split_type(old_board.split_type)
    new_board.set_element_group_type(old_board.element_group_type)


def horizontal_symmetry(element):
    elem_copy = [[value for value in row] for row in element.matrix]
    for i in range(len(elem_copy)):
        for j in range(len(elem_copy[i])):
            element.matrix[i][j] = \
                elem_copy[len(elem_copy)-i-1][j]
    return element

def vertical_symmetry(element):
    elem_copy = [[value for value in row] for row in element.matrix]
    for i in range(len(elem_copy)):
        for j in range(len(elem_copy[i])):
            element.matrix[i][j] = \
                elem_copy[i][len(elem_copy[i])-j-1]
    return element
