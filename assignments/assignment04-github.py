
from github import Github
from github.Auth import Token
import os

apikey = os.getenv("GITHUB_KEY")

auth = Token(apikey)
g = Github(auth=auth)


repo_name = "fin81985/WSAA-coursework"
file_path = "assignments/sample_text.txt"
commit_message = "Replaced 'Andrew' with 'Finian' for assignment04"

try:
    g = Github(apikey)
    repo = g.get_repo(repo_name)

    file = repo.get_contents(file_path)
    content = file.decoded_content.decode("utf-8")

    updated_content = content.replace("Andrew", "Finian")

    if content != updated_content:
        repo.update_file(file_path, commit_message, updated_content, file.sha)
        print("File updated and pushed successfully.")
    else:
        print("No changes needed.")

except Exception as e:
    print(f"Error: {e}")
