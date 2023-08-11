#git_operations.py

from git import Repo
import os
import git
import shutil

def clone_repo(repo_link):
    repo_dir = "./REPO"

    print(f"Attempting to clone repository from {repo_link} into {repo_dir}")

    # Check if the directory exists and remove it if it does
    if os.path.exists(repo_dir):
        print("Directory exists. Removing...")
        shutil.rmtree(repo_dir)

    try:
        print("Cloning repository...")
        git.Repo.clone_from(repo_link, repo_dir)
        print("Repository cloned successfully.")
    except Exception as e: # Catching all exceptions for broader diagnostics
        print(f"An error occurred while cloning the repository: {str(e)}")
        return None

    return repo_dir
