from config import transparent_color
from config import number_of_colors

class Element:
    def __init__(self, matrix, pos, color):
        self.matrix = [[value for value in row] for row in matrix]
        self.pos = (pos[0], pos[1])
        self.color = color
        
        if color is None and len(matrix)>0 and len(matrix[0])>0:
            only_color = transparent_color
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if only_color == transparent_color:
                        only_color = matrix[i][j]
                    elif only_color == -1:
                        break
                    elif only_color != matrix[i][j]:
                        only_color = -1
            if(only_color != transparent_color and 
               only_color != -1):
                self.color = only_color
                


    def copy(self):
        c = Element(self.matrix, self.pos, self.color)
        return c

    @property
    def height(self):
        return len(self.matrix)

    @property
    def width(self):
        if len(self.matrix) == 0:
            return 0
        return len(self.matrix[0])
