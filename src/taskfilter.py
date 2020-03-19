import json
import numpy

def filter_tasks_by_number_of_colors(tasks, min_number_of_colors=0, max_number_of_colors=2, force_black=True):
    return_list = []
    for path in tasks:
        with open(path, 'r') as file:
            task = json.load(file)
        conditions_met = True
        for data in task['train']:

            data_input = data['input']
            data_output = data['output']

            colors_in = get_board_number_of_colors(data_input)
            colors_out = get_board_number_of_colors(data_output)

            if max(colors_in, colors_out) > max_number_of_colors:
                conditions_met = False
                break
            if min(colors_in, colors_out) < min_number_of_colors:
                conditions_met = False
                break
            if force_black and (board_contains_black(data_input) == False or board_contains_black(data_output) == False):
                conditions_met = False
                break
        if conditions_met:
            return_list.append(task)
    #print(len(return_list),'tasks matched the criteria')
    return return_list

def get_board_number_of_colors(board):
    occurences = [0] * 10
    for row in board:
        for num in row:
            occurences[num] = occurences[num]+1
    return numpy.count_nonzero(occurences)

def board_contains_black(board):
    has_black = False
    for row in board:
        for num in row:
            if num == 0:
                has_black = True
                break
        if has_black:
            break
    return has_black
