import base64
from github import Github
from github import InputGitTreeElement

access_token = "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"
g = Github(access_token)
repo = g.get_user().get_repo('CustomJobGael')

file_list = ['C:\CustomJobGael\SystemCommit.py',
             'C:\CustomJobGael\SystemRunner.py',
             'C:\CustomJobGael\SystemRunner.py',
             'C:\CustomJobGael\SystemRunner.xsl']

file_names = ['SystemRunner.py',
              'SystemRunner.xml',
              'SystemCommit.py',
              'SystemRunner.xsl']

commit_message = 'python commit'
master_ref = repo.get_git_ref('head/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

element_list = list()
for i, entry in enumerate(file_list):
    with open(entry) as input_file:
        data = input_file.read()
    if entry.endswith('.png'):
        data = base64.b64encode(data)
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)
    
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)