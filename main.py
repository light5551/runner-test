import sys 
from github import Github

token = sys.argv[1] 
print("first print:")
print(token)
gh = Github(token)
repo = gh.get_repo("light5551/runner-test")
print(repo)
print()
