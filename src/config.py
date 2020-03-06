from pathlib import Path

data_path = Path('data/')
training_path = data_path / 'training'
evaluation_path = data_path / 'evaluation'
test_path = data_path / 'test'

training_tasks = sorted(training_path.iterdir())
evaluation_tasks = sorted(evaluation_path.iterdir())
