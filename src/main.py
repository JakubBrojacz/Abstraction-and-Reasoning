import sys
import config
# import save
from operations import move
import visualize  # noqa
import taskfilter
import board
import json

from splitting import SPLITTING_TYPES
from strategy import ProcessingStrategy


def calculate(input_board, paths):
    input_board.get_elements()
    results = []
    for path in paths:
        output_board = input_board
        for operation, args in path:
            output_board = operation.run(output_board, args)
        results.append(output_board)
    return results


def get_paths_for_input_output_by_operations(
        input_board, output_board, operations, max_matches=sys.maxsize):
    '''
    input: input and output boards, list of operations,
        maximum number of paths returned
    output: list of no more than max_matches paths that transform
        input board to output
    '''
    paths = []
    matches = 0
    for op1 in operations:
        for result1, args1 in op1.try_run(input_board):
            if result1.equals(output_board):
                paths.append([
                    (op1, args1)
                ])
                matches += 1
                if matches >= max_matches:
                    return paths
            for op2 in operations:
                if op1 == op2:
                    continue
                for result2, args2 in op2.try_run(result1):
                    if result2.equals(output_board):
                        paths.append([
                            (op1, args1),
                            (op2, args2)
                        ])
                        matches += 1
                        if matches >= max_matches:
                            return paths
    return paths


def get_paths_for_input_output_set_by_operations(sets, operations,
                                                 max_matches=sys.maxsize):
    '''
    input: sets of input and output boards, list of operations,
        maximum number of paths returned
    output: list of no more than max_matches paths that transform
        each input from set to its output
    remark: first one path is created, then checked for all input-outputs
        in the set
    '''
    paths = []
    matches = 0
    for op1 in operations:
        for result1, args1 in op1.try_run(sets[0][0]):
            if result1.equals(sets[0][1]):
                path = [
                    (op1, args1)
                ]
                matched = True
                for i in range(1, len(sets)):
                    if not is_path_transforming_input_to_output(
                            sets[i][0], sets[i][1], path):
                        matched = False
                        break
                if matched:
                    paths.append(path)
                    matches += 1
                    if matches >= max_matches:
                        return paths
            for op2 in operations:
                if op1 == op2:
                    continue
                for result2, args2 in op2.try_run(result1):
                    if result2.equals(sets[0][1]):
                        path = [
                            (op1, args1),
                            (op2, args2)
                        ]
                        matched = True
                        for i in range(1, len(sets)):
                            if not is_path_transforming_input_to_output(
                                    sets[i][0], sets[i][1], path):
                                matched = False
                                break
                        if matched:
                            paths.append(path)
                            matches += 1
                            if matches >= max_matches:
                                return paths
    return paths


def is_path_transforming_input_to_output(input_board, output_board, path):
    '''
    input: input board, output board, path for calculation
    output: boolean value stating whether output was achieved from input
        via specified path
    '''
    processed_board = input_board.copy()
    for operation, args in path:
        processed_board = operation.run(processed_board, args)
    if processed_board.equals(output_board):
        return True
    return False


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


def process_task(file_path, task, operations, results, strategy):
    prepare_task(task)

    num_test = len(task['test'])
    remaining_result_boards = config.max_result_boards
    result_boards = [[] for i in range(num_test)]

    for split_type in range(SPLITTING_TYPES):
        set_split_type(task, split_type)

        if strategy == ProcessingStrategy.FIRST_ONLY:
            paths = get_paths_for_input_output_by_operations(
                task['train'][0]['input'],
                task['train'][0]['output'],
                operations, remaining_result_boards)

        elif strategy == ProcessingStrategy.ONE_BY_ONE:
            sets = [[] for in_out in task['train']]
            for i in range(len(task['train'])):
                sets[i] = (task['train'][i]['input'],
                           task['train'][i]['output'])
            paths = get_paths_for_input_output_set_by_operations(
                sets, operations, remaining_result_boards)

        for i in range(num_test):
            result_boards[i].extend(calculate(task['test'][i]['input'], paths))
            # save.add_results(results, file_path, i, result_board)
            # task['test'][0]['output'] = result
        remaining_result_boards -= len(paths)
        if remaining_result_boards <= 0:
            break

    correct_results = 0
    total_results = 0
    passed_tests = 0
    for i in range(num_test):
        test_passed = False
        for j in range(len(result_boards[i])):
            total_results += 1
            if result_boards[i][j].matrix == task['test'][i]['output']:
                correct_results += 1
                test_passed = True
        if test_passed:
            passed_tests += 1
    print(passed_tests, '/', num_test, ' tests passed with ',
          correct_results, '/', total_results, ' correct boards ', sep='')


if __name__ == "__main__":
    results = []
    operations = [move.Move]  # TODO
    i = 0

    tasks = []
    for path in config.training_tasks:
        with open(path, 'r') as file:
            tasks.append(json.load(file))

    tasks = taskfilter.filter_tasks_by_max_board_area(
        tasks, config.max_board_area)
    tasks = taskfilter.filter_tasks_by_number_of_colors(
        tasks, config.min_colors, config.max_colors, config.must_have_black)

    for task in tasks:
        i += 1
        print('Task ', i, ': ', sep='', end='')
        # print(task)

        # visualize.plot_task(task)
        process_task("path", task, operations, results,
                     config.processing_strategy)

        # print(task)
    # save.save_results(results, 'submission.csv')
