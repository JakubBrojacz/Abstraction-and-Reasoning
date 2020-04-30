class Dots:
    def get_element_group(board):
        elements = board.elements
        matrix = board.matrix
        result_elements = []
        for element in elements:
            if len(element.matrix) == 1 and\
                    len(element.matrix[0]) == 1:
                result_elements.append(element)
        return result_elements
