import matplotlib.pyplot as plt
from matplotlib import colors

def draw(task, result_boards):
    height = 2 + 2 * len(task['test'])
    width = len(task['train'])
    for result_board in result_boards:
        width = max(width, 1 + len(result_board))

    fig, axs = plt.subplots(height, width)
    for i in range(width):
        for j in range(height):
            axs[j, i].axis('off')
    for i in range(len(task['train'])):
        plot_one(axs[0, i], task['train'][i]['input'].matrix, 'train input ' + str(i + 1))
        plot_one(axs[1, i], task['train'][i]['output'].matrix, 'train output ' + str(i + 1))

    test_number = 1
    for result_board, test_case in zip(result_boards, task['test']):
        plot_one(axs[2 * test_number, 0], test_case['input'].matrix,
            'test input ' + str(test_number))
        plot_one(axs[2 * test_number + 1, 0], test_case['output'],
            'correct answer ' + str(test_number))
        for i in range(len(result_board)):
            plot_one(axs[2 * test_number + 1, i + 1], result_board[i].matrix,
                'test '+str(test_number) + ' answer ' + str(i + 1))
        test_number += 1

    plt.tight_layout()
    plt.show()

def plot_matrix(ax, matrix):
    cmap = colors.ListedColormap(
        ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00',
         '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25',
         '#660066'])
    norm = colors.Normalize(vmin=0, vmax=10)

    ax.imshow(matrix, cmap=cmap, norm=norm)
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)
    ax.set_yticks([x-0.5 for x in range(1+len(matrix))])
    ax.set_xticks([x-0.5 for x in range(1+len(matrix[0]))])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_title("matrix")


def plot_one(ax, matrix, title):
    plot_matrix(ax, matrix)
    ax.set_title(title)
