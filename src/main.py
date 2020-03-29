import config
# import save
from operations import move
# import visualize
import taskfilter
import board

from splitting import SPLITTING_TYPES


class Operation:
    pass  # TODO


def calculate(input_board, paths):
    input_board.get_elements()
    results = []
    for path in paths:
        output_board = input_board
        for operation, args in path:
            output_board = operation.run(output_board, args)
        results.append(output_board)
    return results


def process_input_output(input_board, output_board, operations):
    paths = []
    for op1 in operations:
        # print(op1)
        # print(input_board)
        for result1, args1 in op1.try_run(input_board):
            for op2 in operations:
                for result2, args2 in op2.try_run(result1):
                    if result2.equals(output_board):
                        paths.append([
                            (op1, args1),
                            (op2, args2)
                        ])
                    # if len(paths) >= 3:
                    #     return paths
    return paths


def common(paths):
    '''
    input: list of (lists of paths to solve training task)
        for each training taks
    output: list of most common paths
    '''
    # TODO
    return paths[0]


def prepare_task(task):
    '''
    input: raw dictionary of tasks
    output: dictionary of prepared Board objects
    '''
    num_train = len(task['train'])
    for i in range(num_train):
        task['train'][i]['input'] = board.Board(task['train'][i]['input'])
        task['train'][i]['output'] = board.Board(task['train'][i]['output'])

    num_test = len(task['test'])
    for i in range(num_test):
        task['test'][i]['input'] = board.Board(task['test'][i]['input'])


def set_split_type(task, split_type):
    for train_task in task['train']:
        train_task['input'].set_split_type(split_type)
        train_task['output'].set_split_type(split_type)

    for test_task in task['test']:
        test_task['input'].set_split_type(split_type)


def process_task(file_path, task, operations, results):
    num_train = len(task['train'])
    prepare_task(task)

    for split_type in range(SPLITTING_TYPES):
        # print(split_type)
        # print(task)
        set_split_type(task, split_type)

        paths = [[] for i in range(num_train)]

        for i in range(num_train):
            paths[i] = process_input_output(
                task['train'][i]['input'],
                task['train'][i]['output'],
                operations)

        # if len(paths[0]) > 0:
        # print(paths)

        paths = common(paths)

        num_test = len(task['test'])
        for i in range(num_test):
            result_boards = calculate(task['test'][i]['input'], paths)
            print(result_boards)
            # save.add_results(results, file_path, i, result_board)
            # task['test'][0]['output'] = result


if __name__ == "__main__":
    results = []
    operations = [move.Move]  # TODO
    i = 0
    for task in taskfilter.filter_tasks_by_number_of_colors(
            config.training_tasks, 0, 2, True):

        i += 1
        print(i)
        # print(task)

        process_task("path", task, operations, results)
        # print(task)
        # visualize.plot_task(task)
    # save.save_results(results, 'submission.csv')
