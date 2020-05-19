class ExceptDots:
    def get_element_group(board):
        elements = board.elements
        result_elements = []
        for element in elements:
            if element.height != 1 and\
                    element.width != 1:
                result_elements.append(element)
        return result_elements
