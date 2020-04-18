import config
# import save
# from operations import move
import operations
import visualize  # noqa
import taskfilter
import board
import json
import strategies

from splitting import SPLITTING_TYPES
from strategies.strategy import ProcessingStrategy


def calculate(input_board, paths):
    input_board.get_elements()
    results = []
    for path in paths:
        output_board = input_board
        for operation, args in path:
            output_board = operation.run(output_board, args)
        results.append(output_board)
    return results


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


def show_results(task, result_boards):
    correct_results = 0
    total_results = 0
    passed_tests = 0
    for result_board, test_case in zip(result_boards, task['test']):
        test_passed = False
        for try_board in result_board:
            total_results += 1
            if try_board.matrix == test_case['output']:
                correct_results += 1
                test_passed = True
        if test_passed:
            passed_tests += 1
    print(f'{passed_tests}/{len(task["test"])} tests passed with '
          f'{correct_results}/{total_results} correct boards ')


def process_task(file_path, task, operation_list, results, strategy):
    prepare_task(task)

    num_test = len(task['test'])
    remaining_result_boards = config.max_result_boards
    result_boards = [[] for i in range(num_test)]

    for split_type in range(SPLITTING_TYPES):
        set_split_type(task, split_type)

        paths = strategy.solve(task, operation_list, remaining_result_boards)

        for i in range(num_test):
            result_boards[i].extend(calculate(task['test'][i]['input'], paths))
            # save.add_results(results, file_path, i, result_board)
            # task['test'][0]['output'] = result
        remaining_result_boards -= len(paths)
        if remaining_result_boards <= 0:
            break

    show_results(task, result_boards)


if __name__ == "__main__":
    results = []
    operation_list = [operations.Move]  # TODO
    i = 0

    if config.processing_strategy == ProcessingStrategy.FIRST_ONLY:
        strategy = strategies.first_only.FirstOnlyStrategy()
    elif config.processing_strategy == ProcessingStrategy.ONE_BY_ONE:
        strategy = strategies.one_by_one.OneByOneStrategy()
    else:
        raise Exception("Bad strategy type")

    tasks = []
    for path in config.training_tasks:
        with open(path, 'r') as file:
            tasks.append(json.load(file))
            tasks[-1]["name"] = path

    tasks = taskfilter.filter_tasks_by_max_board_area(
        tasks, config.max_board_area)
    tasks = taskfilter.filter_tasks_by_number_of_colors(
        tasks, config.min_colors, config.max_colors, config.must_have_black)

    for task in tasks:
        i += 1
        print(task["name"])
        print(f'Task {i}: ', end='')

        # visualize.plot_task(task)
        process_task("path", task, operation_list, results,
                     strategy)

        # print(task)
    # save.save_results(results, 'submission.csv')
