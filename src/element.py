class Element:
    def __init__(self, matrix, pos, color):
        self.matrix = [[value for value in row] for row in matrix]
        self.pos = (pos[0], pos[1])
        self.color = color

    def copy(self):
        c = Element(self.matrix, self.pos, self.color)
        return c
