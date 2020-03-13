import copy
import json

import config
import visualize

class Operation:
    pass#todo


class Information:
    pass#todo


class Results:
    pass#todo


def calculate(input, info, operations):
    input.get_objects()
    results = []
    paths = info.get_paths()
    for operations in paths:
        output = copy.deepcopy(input)
        for operation in operations:
            output = operation.exec(output)
        results.append(output)
    return results


def process_input_output(info, input, output):
    input.get_objects()
    output.get_objects()
    num_divisions = len(input.objects)
    for i in range(num_divisions):
        for op1 in operations:
            for op2 in operations:
                if op2.exec(op1.exec(input)).equals(output)
                    info.add_path([op1, op2])


def process_task(id, task, operations, results):
    info = new Information()

    num_train = len(task['train'])
    for i in range(num_train):
        process_input_output(task['train'][i]['input'], task['train'][i]['output'], info, operations)

    num_test = len(task['test'])
    for i in range(num_test):
        result = calculate(task['test'][i]['input'], info)
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
    operations = []
    for i in range(len(config.training_tasks)):
        with open(config.training_tasks[i], 'r') as f:
            task = json.load(f)

        print(i)
        print(config.training_tasks[i])
        # process_task(config.training_tasks[i], task, operations, results)
        # print(task)
        visualize.plot_task(task)
    results.save('submission.csv')
