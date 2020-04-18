class AtEdge:
    def get_element_group(matrix, elements):
        result_elements = []
        for element in elements:
            if element.pos[0] == 0 or\
                    element.pos[1] == 0 or\
                    element.pos[0] + len(element.matrix) == len(matrix) or\
                    element.pos[1] + len(element.matrix[0]) == len(matrix[0]):
                result_elements.append(element.copy())
        return result_elements
