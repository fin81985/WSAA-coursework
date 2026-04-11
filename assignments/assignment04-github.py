
from config import config
from github import Github
from github.Auth import Token

apikey = config.get("github_key") # Get the github api key from the config file

auth = Token(apikey) # Authenticate to github using the token from the config
g = Github(auth=auth) # Create a github object using the authenticated token


# Repo details
repo_name = "fin81985/WSAA-coursework"
file_path = "assignments/sample_text.txt"
commit_message = "Replaced 'Andrew' with 'Finian' for assignment04"

try:
    repo = g.get_repo(repo_name)# Get the repo object for the repo we want to update

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


