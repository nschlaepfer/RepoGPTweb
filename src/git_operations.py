from git import Repo
import os
import git
import shutil  # Needed for removing directory

def clone_repo(repo_link):
    repo_dir = "./REPO"

    # Check if the directory exists and remove it if it does
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)

    git.Repo.clone_from(repo_link, repo_dir)
    
    return repo_dir
