import sys 
from github import Github

token = sys.argv[1] 
number_pr = sys.argv[2]
print("first print:")
print(token)
print(number_pr)
gh = Github(token)
repo = gh.get_repo("light5551/runner-test")
pull = repo.get_pull(int(number_pr))
pull_issue = repo.get_issue(pull.number)
pull_issue.add_to_labels("Github action works fine!")
#pull.edit(state='closed')




