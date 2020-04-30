from config import number_of_colors, background_color


class ContainsUniqueColor:
    def get_element_group(board):
        elements = board.elements
        matrix = board.matrix
        contains_color_count = [0] * (number_of_colors + 1)
        for element in elements:
            contains_color = [0] * (number_of_colors + 1)
            for row in element.matrix:
                for field in row:
                    if field != background_color:
                        contains_color[field] = 1
            for color in range(len(contains_color_count)):
                contains_color_count[color] += contains_color[color]
        unique_color = -1
        for color in range(len(contains_color_count)):
            if contains_color_count[color] == 1:
                if unique_color == -1:
                    unique_color = color
                else:
                    return []
        if unique_color == -1:
            return []
        for element in elements:
            for row in element.matrix:
                for field in row:
                    if field == unique_color:
                        return [element.copy()]
        return []
