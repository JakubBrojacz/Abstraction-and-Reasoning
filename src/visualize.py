import json

import matplotlib.pyplot as plt
from matplotlib import colors

import config


def plot_one(ax, task, i, train_or_test, input_or_output):
    cmap = colors.ListedColormap(
        ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00',
         '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25',
         '#660066'])
    norm = colors.Normalize(vmin=0, vmax=10)

    input_matrix = task[train_or_test][i][input_or_output]
    ax.imshow(input_matrix, cmap=cmap, norm=norm)
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)
    ax.set_yticks([x-0.5 for x in range(1+len(input_matrix))])
    ax.set_xticks([x-0.5 for x in range(1+len(input_matrix[0]))])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title(train_or_test + ' '+input_or_output)


def plot_task(task):
    """
    Plots the first train and test pairs of a specified task,
    using same color scheme as the ARC app
    """
    num_train = len(task['train'])
    fig, axs = plt.subplots(2, num_train, figsize=(3*num_train, 3*2))
    for i in range(num_train):
        plot_one(axs[0, i], task, i, 'train', 'input')
        plot_one(axs[1, i], task, i, 'train', 'output')
    plt.tight_layout()
    plt.show()

    num_test = len(task['test'])
    fig, axs = plt.subplots(2, num_test, figsize=(3*num_test, 3*2))
    if num_test == 1:
        plot_one(axs[0], task, 0, 'test', 'input')
        plot_one(axs[1], task, 0, 'test', 'output')
    else:
        for i in range(num_test):
            plot_one(axs[0, i], task, i, 'test', 'input')
            plot_one(axs[1, i], task, i, 'test', 'output')
    plt.tight_layout()
    plt.show()


def plot_array(task):
    num_train = len(task['test'])
    fig, axs = plt.subplots(1, num_train, figsize=(3*num_train, 3*1))
    for i in range(num_train):
        plot_one(axs[0, i], task, i, 'test', 'output')
    plt.tight_layout()
    plt.show()


def plot_output(output):
    data = {"test": [{"output": output}]}
    task = json.dumps(data)
    plot_array(task)


if __name__ == "__main__":
    for i in range(len(config.training_tasks)):
        with open(config.training_tasks[i], 'r') as f:
            task = json.load(f)

        print(i)
        print(config.training_tasks[i])
        plot_task(task)
