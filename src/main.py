import copy

import config
import save
import visualize
import taskfilter


class Operation:
    pass  # TODO


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
                if op2.exec(op1.exec(input)).equals(output):
                    paths.append([op1, op2])
                if len(paths) >= 3:
                    return


def process_task(file_path, task, operations, results):
    paths = []

    num_train = len(task['train'])
    for i in range(num_train):
        process_input_output(task['train'][i]['input'],
                             task['train'][i]['output'], operations, paths)

    num_test = len(task['test'])
    for i in range(num_test):
        result = calculate(task['test'][i]['input'], paths)
        save.add_results(results, file_path, i, result)
        # task['test'][0]['output'] = result


if __name__ == "__main__":
    # results = Results()

    operations = []  # TODO
    for task in taskfilter.filter_tasks_by_number_of_colors(
            config.training_tasks, 0, 2, True):

        print(task)

        # process_task(config.training_tasks[i], task, operations, results)
        # print(task)
        visualize.plot_task(task)
    # save.save_results(results, 'submission.csv')
