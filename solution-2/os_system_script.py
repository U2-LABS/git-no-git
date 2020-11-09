import os # or it can be subprocess.call()

git_repo_path = 'git-no-git/' # Name of the repo to work with

# Change working dir to git repo
os.chdir(git_repo_path)

# Create test files in repo
for x in range(1, 4):
    fname = f'filename{x}'
    folder_name = f'folder#{x}'
    with open(fname, 'w') as f:
        f.write('test_data')
    os.mkdir(folder_name)

# Add/Commit data
os.system(f'git add .')
os.system('git commit -m "next commit"')
