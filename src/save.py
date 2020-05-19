

class Save:
    def __init__(self):
        self.results = []

    def add_results(self, result_boards, file_path):
        # result boards to jest tablica tablic
        # W każdym tasku może być kilka zapytań
        # Żeby uzyskać odpowiedź na task_id_0 trzeba się odwoływać
        # do result_boards[0].
        file_name = file_path.stem
        for test_case, test_result_boards in enumerate(result_boards):
            result = f'{file_name}_{test_case},'
            for test_result_board in test_result_boards:
                result += flattener(test_result_board.matrix)
            result += '\n'
            self.results.append(result)

    def save_results(self, file_name):
        with open(file_name, 'w') as file:
            file.write("output_id,output\n")
            for result in self.results:
                file.write(result)


def flattener(matrix):
    result = '|'
    for row in matrix:
        for color in row:
            result += str(color)
        result += '|'
    result += ' '
    return result
