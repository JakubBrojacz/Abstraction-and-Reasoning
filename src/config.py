from pathlib import Path

data_path = Path('data/')
training_path = data_path / 'training_sample'
# training_path = data_path / 'training'

training_tasks = sorted(training_path.iterdir())

processing_strategy = "ONE_BY_ONE"
max_result_boards = 3
max_board_area = 128
min_colors = 0
max_colors = 4
must_have_black = True

background_color = 0
transparent_color = 10
number_of_colors = 10

max_board_dimension_size = 30