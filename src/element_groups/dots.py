class Dots:
    def get_element_group(board):
        elements = board.elements
        matrix = board.matrix
        result_elements = []
        for element in elements:
            if element.height == 1 and\
                    element.width == 1:
                result_elements.append(element)
        return result_elements
