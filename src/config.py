from pathlib import Path
import strategy

data_path = Path('data/')
training_path = data_path / 'training_sample'
training_path = data_path / 'training'
evaluation_path = data_path / 'evaluation'
test_path = data_path / 'test'

training_tasks = sorted(training_path.iterdir())
evaluation_tasks = sorted(evaluation_path.iterdir())

processing_strategy = strategy.ProcessingStrategy.ONE_BY_ONE
max_result_boards = 3
