import os

dirs = [
    os.path.join('data', 'row'),
    os.path.join('data', 'processed'),
    'notebooks',
    'saved model',
    'src'

]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open (os.path.join(dir_, 'gitkeep'), 'w') as f:
        pass
files = [
    'dvc.yaml',
    'params.yaml',
    'gitignore',
    os.path.join('src', '__init__.py')

]
for file in files:
    with open(file, 'w') as f:
        pass