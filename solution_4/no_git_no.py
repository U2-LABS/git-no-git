import pygit2
import os

current_working_directory = os.getcwd()
repository_path = pygit2.discover_repository(current_working_directory)
repo = pygit2.Repository(repository_path)

index = repo.index

# Create test files in repo
for x in range(1, 4):
    fname = f'filename{x}'

    with open(fname, 'w') as f:
        f.write('test_data')
    index.add(fname) # add file. Replace `git add filename`
    index.write() # write filename in index


commit = repo[repo.head.target] # get info about last commit
master = repo.branches.get('master') # get info about our branch master
tree_id = repo.index.write_tree() # create contests of index that will be written out to the object database
committer = pygit2.Signature('Nikita Efremov', 'nikefremov.00.008@hotmail.com') # create commiter (who will create commit)
repo.create_commit(master.name,commit.author, commit.author, 'Commit from python',tree_id, [master.target]) # create commmit
