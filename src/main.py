import copy
import json

import config
import visualize
import taskfilter

class Operation:
    pass#todo


class Results:
    pass#todo


def calculate(input, paths):
    input.get_objects()
    results = []
    for path in paths:
        output = copy.deepcopy(input)
        for operation in path:
            output = operation.exec(output)
        results.append(output)
    return results

def equals(self, output):
    for i in range(len(self)):
        for j in range(len(self[i])):
            if self[i][j] != output[i][j]:
                return False
    return True

def process_input_output(input, output, operations, paths):
    input.get_objects()
    output.get_objects()
    num_divisions = len(input.objects)
    for i in range(num_divisions):
        for op1 in operations:
            for op2 in operations:
                if op2.exec(op1.exec(input)).equals(output)
                    paths.append([op1, op2])


def process_task(id, task, operations, results):
    paths = []

    num_train = len(task['train'])
    for i in range(num_train):
        process_input_output(task['train'][i]['input'], task['train'][i]['output'], operations, paths)

    num_test = len(task['test'])
    for i in range(num_test):
        result = calculate(task['test'][i]['input'], paths)
        results.add(id, result)
        # task['test'][0]['output'] = result


# def flattener(pred):
#     str_pred = str([row for row in pred])
#     str_pred = str_pred.replace(', ', '')
#     str_pred = str_pred.replace('[[', '|')
#     str_pred = str_pred.replace('][', '|')
#     str_pred = str_pred.replace(']]', '|')
#     return str_pred


if __name__ == "__main__":
    results = new Results()

    operations = []#todo
    for task in taskfilter.filter_tasks_by_number_of_colors(config.training_tasks,0,2,True):

        print(task)
        # process_task(config.training_tasks[i], task, operations, results)
        # print(task)
        visualize.plot_task(task)
    results.save('submission.csv')
