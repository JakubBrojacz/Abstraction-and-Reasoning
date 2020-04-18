from . import main_splitting


class ColorSplit:
    def get_elements(matrix):
        return main_splitting.split_only_by_color(
            matrix, 0, 10, 10
        )


class FourWayConnectedSingleColor:
    def get_elements(matrix):
        return main_splitting.split(
            matrix, 0, 10, 4, True
        )


class EightWayConnectedSingleColor:
    def get_elements(matrix):
        return main_splitting.split(
            matrix, 0, 10, 8, True
        )


class FourWayConnectedMultiColor:
    def get_elements(matrix):
        return main_splitting.split(
            matrix, 0, 10, 4, False
        )


class EightWayConnectedMultiColor:
    def get_elements(matrix):
        return main_splitting.split(
            matrix, 0, 10, 8, False
        )
