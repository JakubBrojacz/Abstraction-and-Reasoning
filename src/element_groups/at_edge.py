class AtEdge:
    def get_element_group(board):
        elements = board.elements
        result_elements = []
        for element in elements:
            if element.pos[0] == 0 or\
                    element.pos[1] == 0 or\
                    element.pos[0] + element.height == board.height or\
                    element.pos[1] + element.width == board.width:
                result_elements.append(element)
        return result_elements
