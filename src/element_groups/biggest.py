class Biggest:
    def get_element_group(matrix, elements):
        result_elements = []
        max_area = 0
        for element in elements:
            if len(element.matrix) * len(element.matrix[0]) > max_area:
                max_area = len(element.matrix) * len(element.matrix[0])
        for element in elements:
            if len(element.matrix) * len(element.matrix[0]) == max_area:
                result_elements.append(element.copy())
        return result_elements
