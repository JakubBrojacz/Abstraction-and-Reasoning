import json
import numpy
from pandas.io.json import json_normalize

class TaskFilter:
    def __init__(self, tasks_input):
        self.tasks=tasks_input

    def filter_tasks_by_number_of_colors(self, min_number_of_colors = 0, max_number_of_colors=2, force_black=True):
        list = []
        for i in range(len(self.tasks)):
            with open(self.tasks[i], 'r') as f:
                task = json.load(f)
                conditions_met=True
                for data in task['train']:

                    input = data['input']
                    output = data['output']

                    colors_in = self.__get_board_number_of_colors(input)
                    colors_out = self.__get_board_number_of_colors(output)

                    if(max(colors_in,colors_out)>max_number_of_colors):
                        conditions_met=False
                        break
                    if(min(colors_in,colors_out)<min_number_of_colors):
                        conditions_met=False
                        break
                    if(force_black and (self.__board_contains_black(input)==False or self.__board_contains_black(output)==False)):
                        conditions_met=False
                        break
                if(conditions_met):
                    list.append(task)
        print(len(list))
        return list

    def __get_board_number_of_colors(self, board):
        occurences = [0] * 10
        for row in board:
            for num in row:
                occurences[num]=occurences[num]+1
        return numpy.count_nonzero(occurences)

    def __board_contains_black(self, board):
        has_black = False
        for row in board:
            for num in row:
                if(num==0):
                    has_black=True
                    break
            if(has_black):
                break
        return has_black