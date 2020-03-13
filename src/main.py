import json

import config
import visualize


def process_task(task):
    pass


if __name__ == "__main__":
    for i in range(len(config.training_tasks)):
        with open(config.training_tasks[i], 'r') as f:
            task = json.load(f)

        print(i)
        print(config.training_tasks[i])
        # process_task(task)
        # print(task)
        visualize.plot_task(task) 
