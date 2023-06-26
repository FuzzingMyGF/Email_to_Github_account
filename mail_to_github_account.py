import requests
import json

def create_github_repo(repo_name, token):
    # Create a new private GitHub repository
    headers = {
        "Authorization": "Bearer " + token
    }
    data = {
        "name": repo_name,
        "private": True,
        "auto_init": True
    }
    response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
    if response.status_code == 201:
        print("The new GitHub project has been created successfully.")
    else:
        print("An error occurred while creating the GitHub project.")

def commit_to_github(repo_name, email, token,username):
    # Perform a commit on the GitHub repository
    headers = {
        "Authorization": "Bearer " + token   
    }
    data = {
        "message": "Initial commit",
        "committer": {
            "name": "test",
            "email": email
        },
        "content": "T1NJTlQ="
    }
    response = requests.put(f"https://api.github.com/repos/{username}/{repo_name}/contents/test.txt", headers=headers, json=data)
    if response.status_code == 201:
        print("The commit has been performed successfully.")
    else:
        print("An error occurred during the commit.")

def get_commit_author(repo_name, token,username):
    # Get the author of the latest commit on the GitHub repository
    headers = {
        "Authorization": "Bearer " + token
    }
    response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/commits", headers=headers)
    if response.status_code == 200:
        commits = response.json()
        if len(commits) > 0:
            if not commits[0]['author']['login']:
                print("Account configured to block fake git push")
                return

            commit_author = commits[0]['author']['login']
            commit_author_id = commits[0]['author']['id']
            
            print("The name of the author of the latest commit is:", commit_author)
            print("The ID of the account is:", commit_author_id)
        else:
            print("No commits found in the project.")
    else:
        print("An error occurred while retrieving the commit author.")

def delete_github_repo(repo_name, token,username):
    # Delete the GitHub repository
    headers = {
        "Authorization": "Bearer " + token
    }
    response = requests.delete(f"https://api.github.com/repos/{username}/{repo_name}", headers=headers)
    if response.status_code == 204:
        print("The GitHub project has been deleted successfully.")
    else:
        print("An error occurred while deleting the GitHub project.")

repo_name = input("Enter the name of the new GitHub project: ")
git_token = input("Enter your GitHub API Token: ")
git_username = input("Enter your GitHub username: ")
create_github_repo(repo_name, git_token)
email = input("Enter the email address for the commit: ")
commit_to_github(repo_name, email, git_token,git_username)
get_commit_author(repo_name, git_token,git_username)
delete_github_repo(repo_name, git_token,git_username)
