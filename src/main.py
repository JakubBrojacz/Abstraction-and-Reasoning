import json

import config
import visualize
import taskfilter


def process_task(task):
    pass


if __name__ == "__main__":
    for task in taskfilter.filter_tasks_by_number_of_colors(config.training_tasks,0,2,True):
        # process_task(task)
        # print(task)
        visualize.plot_task(task)
