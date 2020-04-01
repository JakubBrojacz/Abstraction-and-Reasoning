import config
# import save
from operations import move
# import visualize
import taskfilter
import board
import sys

from splitting import SPLITTING_TYPES
from enum import Enum

class ProcessingStrategy(Enum):
    FIRST_ONLY = 1
    FIRST_THEN_OTHERS = 2
    ONE_BY_ONE = 3

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

def get_paths_for_input_output_by_operations(input_board, output_board, operations, max_matches=sys.maxsize):
    paths = []
    matches = 0
    for op1 in operations:
        for result1, args1 in op1.try_run(input_board):
            #if result1.equals(output_board):
            #    paths.append([
            #    (op1, args1)
            #    ])
            #    matches+=1
            #    if(matches>=max_matches):
            #        return paths
            for op2 in operations:
                if op1 == op2: #TODO check czy matchuje
                    continue
                for result2, args2 in op2.try_run(result1):
                    if result2.equals(output_board):
                        paths.append([
                            (op1, args1),
                            (op2, args2)
                        ])
                        matches+=1
                        if(matches>=max_matches):
                            return paths
    return paths

def get_paths_for_input_output_set_by_operations(sets, operations, max_matches=sys.maxsize):
    paths = []
    matches = 0
    for op1 in operations:
        for result1, args1 in op1.try_run(sets[0][0]):
            for op2 in operations:
                if op1 == op2: #TODO check czy matchuje
                    continue
                for result2, args2 in op2.try_run(result1):
                    if result2.equals(sets[0][1]):
                        path = [
                            (op1, args1),
                            (op2, args2)
                        ]
                        matched = True
                        for i in range (1, len(sets)):
                            if not is_path_transforming_input_to_output(sets[i][0],sets[i][1],path):
                                matched = False
                                break
                        if matched:
                            paths.append()
                            matches+=1
                            if(matches>=max_matches):
                                return paths
    return paths

def get_paths_for_input_output_by_paths(input_board, output_board, input_paths):
    output_paths = []
    for path in input_paths:
        if is_path_transforming_input_to_output(input_board, output_board, path):
            output_paths.append(path)
    return output_paths

def is_path_transforming_input_to_output(input_board, output_board, path):
    processed_board = input_board.copy()
    for transformation in path:
        processed_board = transformation[0].run(processed_board,transformation[1])
    if(processed_board.equals(output_board)):
        return True
    return False


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


def process_task(file_path, task, operations, results, strategy):
    num_train = len(task['train'])
    prepare_task(task)

    for split_type in range(SPLITTING_TYPES):
        # print(split_type)
        # print(task)
        set_split_type(task, split_type)

        if strategy == ProcessingStrategy.FIRST_ONLY:
            paths = get_paths_for_input_output_by_operations(
                    task['train'][0]['input'],
                    task['train'][0]['output'],
                    operations, 3)

        elif strategy == ProcessingStrategy.FIRST_THEN_OTHERS:
            paths = paths = get_paths_for_input_output_by_operations(
                    task['train'][0]['input'],
                    task['train'][0]['output'],
                    operations)

            for i in range(1, num_train-1):
                paths = get_input_output_matching_paths(
                    task['train'][i]['input'],
                    task['train'][i]['output'],
                    paths)

        elif strategy == ProcessingStrategy.ONE_BY_ONE:
            sets = [[] for in_out in task['train']]
            for i in range(task['train']):
                sets[i]=(task['train'][i]['input'],
                         task['train'][i]['output'])
            paths = get_paths_for_input_output_set_by_operations(sets,operations,3)

        # if len(paths[0]) > 0:
        # print(paths)

        paths = paths[0:3]

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
        print('First only');
        process_task("path", task, operations, results, ProcessingStrategy.FIRST_ONLY)
        print('First then others');
        process_task("path", task, operations, results, ProcessingStrategy.FIRST_THEN_OTHERS)
        print('One by one');
        process_task("path", task, operations, results, ProcessingStrategy.ONE_BY_ONE)
        # print(task)
        # visualize.plot_task(task)
    # save.save_results(results, 'submission.csv')
