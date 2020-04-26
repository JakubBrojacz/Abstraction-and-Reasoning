class Dots:
    def get_element_group(matrix, elements):
        result_elements = []
        for element in elements:
            if len(element.matrix) == 1 and\
                    len(element.matrix[0]) == 1:
                result_elements.append(element)
        return result_elements
