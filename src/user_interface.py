# src/user_interface.py
#DUMMY UI

import re
import threading


def long_running_operation(repo_link, user_choice):
    # Here goes your long running operation
    pass

def get_user_input():
    print("Welcome to the GitHub Repository Analyzer!")
    
    # Input validation for repository link
    while True:
        repo_link = input("Please enter the link to the GitHub repo you want to analyze: ")
        if validate_repo_link(repo_link):
            break
        else:
            print("Invalid repository link. Please enter a valid GitHub repository link.")
    
    print("Select an operation: ")
    print("1. Convert the code into embeddings and upload to Pinecone.")
    print("2. Comment all files, create README, and a file structure guide.")
    print("3. Perform both operations.")
    
    # Input validation for user choice
    while True:
        user_choice = input("Your choice (1/2/3): ")
        if validate_user_choice(user_choice):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    
    return repo_link, user_choice

def validate_repo_link(link):
    pattern = re.compile(r'https://github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+/?')
    return bool(pattern.match(link))

def validate_user_choice(choice):
    return choice in ['1', '2', '3']

if __name__ == "__main__":
    try:
        repo_link, user_choice = get_user_input()
        print(f"Received repo link: {repo_link}")
        print(f"User's choice: {user_choice}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
