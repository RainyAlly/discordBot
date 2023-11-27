import requests
from dotenv import load_dotenv, dotenv_values, set_key
import os
import time

os.system('cls')
load_dotenv()

RepoOwner = "RainyAlly"
RepoName = "discordBot"

def check_any_commit(RepoOwner, RepoName):
    url = f'https://api.github.com/repos/{RepoOwner}/{RepoName}/commits'
    response = requests.get(url)
    
    if response.status_code == 200:
        Commits = response.json()
        return len(Commits)
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return False
    
def ReadVersion():
    Version = os.getenv("VERSION_CONTROL")
    return int(Version)

Commits = check_any_commit(RepoOwner, RepoName)

def OverVersion(Commits):
    file_path = '.env'
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if line.startswith(f'VERSION_CONTROL='):
            lines[i] = f'VERSION_CONTROL={Commits}\n'
            break
    with open(file_path, 'w') as file:
        file.writelines(lines)

while True:
    Version = ReadVersion()
    while Commits == Version:
        Commits = check_any_commit(RepoOwner, RepoName)
        if Commits == Version:
            print(f"{RepoName} hasn't had any new commits made.")
        elif type(Commits) == "int":
            print(f"A commit has been made in {RepoName}.")
            OverVersion(Commits)
        else:
            print("There was a error")
            Commits = Version
        time.sleep(2.5)
