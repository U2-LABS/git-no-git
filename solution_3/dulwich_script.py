import glob
import os
from dulwich.repo import Repo

# Get repo path 
repo_path = input('Enter the path for your repo(use . for the current dir): ')

repo = Repo(repo_path)

# Create test files
for i in range(1, 5):
    os.mkdir(f'{repo_path}/TestDir{i}')
    with open(f'{repo_path}/TestDir{i}/test.txt', 'w') as f:
        f.write('some data')

# Git add and git commit files
repo.stage([path.split('/', 1)[-1].encode('utf-8') for path in glob.glob(f'{repo_path}/**/*.txt', recursive=True)])
repo.do_commit(b'Add test files')
