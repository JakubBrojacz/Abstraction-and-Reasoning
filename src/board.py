import splitting


class Board:
    def __init__(self, matrix):
        self.matrix = [
            [element for element in row]
            for row in matrix]
        if len(self.matrix) == 0:
            raise Exception("BAD MATRIX")
        self.divisions = None
        self.split_type = 0
        self.get_elements()

    def copy(self):
        c = Board(self.matrix)
        c.divisions = [
            [element.copy() for element in division]
            for division in self.divisions]
        c.set_split_type(self.split_type)
        return c

    def get_elements(self):
        self.divisions = splitting.get_elements(self.matrix)

    def set_split_type(self, split_type):
        self.split_type = split_type

    def equals(self, board2):
        if len(self.matrix) != len(board2.matrix):
            return False
        if len(self.matrix[0]) != len(board2.matrix[0]):
            return False

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != board2.matrix[i][j]:
                    return False

        return True

    def clean_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = 0  # Background color

    def draw_element(self, element):
        x_offset = element.pos[0]
        y_offset = element.pos[1]
        # print(self.matrix)
        # print(element.matrix)
        # print(element.pos)
        for i in range(len(element.matrix)):
            for j in range(len(element.matrix[i])):
                if element.matrix[i][j] != 10:
                    self.matrix[i+x_offset][j+y_offset] = element.matrix[i][j]

    def redraw(self):
        self.clean_matrix()
        for element in self.elements:
            self.draw_element(element)
        return self

    @property
    def height(self):
        return len(self.matrix)

    @property
    def width(self):
        return len(self.matrix[0])

    @property
    def elements(self):
        return self.divisions[self.split_type]
