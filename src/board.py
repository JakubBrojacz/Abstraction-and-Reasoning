from config import transparent_color
from config import number_of_colors


class Board:
    def __init__(self, matrix):
        self.matrix = [
            [element for element in row]
            for row in matrix]
        if len(self.matrix) == 0:
            raise Exception("BAD MATRIX")
        self.elements = None
        self.element_group = None
        self.element_group_counter = None
        self.split_type = None
        self.element_group_type = None
        self.expected_result = None

    def copy(self):
        c = self.copy_empty()
        c.elements = [element.copy() for element in self.elements]
        c.element_group = [element.copy() for element in self.element_group]
        c.element_group_counter = [element.copy()
                                   for element in self.element_group_counter]
        return c

    def copy_empty(self):
        c = Board(self.matrix)
        c.elements = []
        c.element_group = []
        c.element_group_counter = []
        c.split_type = self.split_type
        c.element_group_type = self.element_group_type
        c.expected_result = self.expected_result
        return c

    def set_split_type(self, split_type):
        self.split_type = split_type
        self.elements = split_type.get_elements(self.matrix)

    def set_element_group_type(self, element_group_type):
        self.element_group_type = element_group_type
        element_group = element_group_type.get_element_group(self)
        self.element_group = [element.copy() for element in element_group]
        self.element_group_counter = [element.copy()
                                      for element in self.elements
                                      if element not in element_group]
        # self.element_group = [element.copy() for element in self.elements
        #                       if element in element_group]
        # self.element_group_counter = [element.copy()
        #                               for element in self.elements
        #                               if element not in element_group]

    def equals(self, board2):
        if self.height != board2.height:
            return False
        if self.width != board2.width:
            return False

        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] != board2.matrix[i][j]:
                    return False

        return True

    def clean_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = 0  # Background color

    def draw_element(self, element):
        y_offset = element.pos[0]
        x_offset = element.pos[1]
        # print(self.matrix)
        # print(element.matrix)
        # print(element.pos)
        for i in range(element.height):
            for j in range(len(element.matrix[i])):
                if element.matrix[i][j] != transparent_color:
                    self.matrix[i+y_offset][j+x_offset] = element.matrix[i][j]

    def redraw(self):
        self.clean_matrix()
        for element in self.element_group_counter:
            self.draw_element(element)
        for element in self.element_group:
            self.draw_element(element)
        return self

    @property
    def height(self):
        return len(self.matrix)

    @property
    def width(self):
        if len(self.matrix) == 0:
            return 0
        return len(self.matrix[0])

    @property
    def colors(self):
        is_color = [False for col in range(number_of_colors)]
        for i in range(self.height):
            for j in range(self.width):
                is_color[self.matrix[i][j]] = True
        colors = []
        for i in range(len(is_color)):
            if is_color[i]:
                colors.append(i)
        return colors
