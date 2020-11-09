from git import Repo
import os

repo = Repo(os.getcwd())
index = repo.index

for x in range(1, 4):
    fname = f'filename{x}'
    with open(fname, 'w') as f:
        f.write('b')
    index.add(fname)

index.commit('next commit')
