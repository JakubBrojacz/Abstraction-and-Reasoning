class Biggest:
    def get_element_group(board):
        elements = board.elements
        matrix = board.matrix
        result_elements = []
        max_area = 0
        for element in elements:
            if element.height * element.width > max_area:
                max_area = element.height * element.width
        for element in elements:
            if element.height * element.width == max_area:
                result_elements.append(element)
        return result_elements
