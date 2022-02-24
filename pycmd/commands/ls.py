import os
from github import Github
from time import sleep
from textwrap import dedent
from json import load as read
from pycmd.utils.pycmd import argparse
from dotenv import load_dotenv, get_key
from colorama import Fore as fc, Back as bg, init

init(autoreset=True)
load_dotenv()

print()

def list_folders(path):
    listdir_path = os.listdir(path)
    folders = []
    for file in listdir_path:
        filename, file_extension = os.path.splitext(file)
        file_extension = str(file_extension)
        if file_extension:
            continue
        else:
            folders.append(filename)
    return folders


def list_repos():

    try:
        token = get_key(".env", "GITHUB_TOKEN")
        gh = Github(token)

        user = gh.get_user()
        repos = user.get_repos()

        for i in repos:
            if i.private:
                print(fc.LIGHTBLACK_EX + "• " + i.name)
            else:
                print(fc.LIGHTBLACK_EX + "• " + fc.RESET + i.name)
            sleep(0.1)
    except Exception as e:
        print(bg.RED + "ERR" + bg.RESET + " " + str(e))
        exit(1)


def list_dir(path):

    try:
        projects = list_folders(path)

        print(f'You have {fc.CYAN}{len(projects)}{fc.GREEN} {language} projects\n')

        for i in projects:
            is_empty = True if os.listdir(path + "/" + i) == [] else False
            is_git_init = True if ".git" in os.listdir(path + "/" + i) else False

            if is_empty:
                print(fc.LIGHTBLACK_EX + "• " + i)
            elif is_git_init:
                print(fc.LIGHTBLACK_EX + "• " + fc.GREEN + i)
            else:
                print(fc.LIGHTBLACK_EX + "• " + fc.RESET + i)
            sleep(0.1)
    except Exception as e:
        print(bg.RED + "ERR" + bg.RESET + " " + str(e))
        exit(1)


project, flags = argparse()
language = ""

if project == "py" or project == "python":
    language = "python"

elif project == "js" or project == "nodejs":
    language = "javascript"

elif project == "java":
    language = "java"

elif project == "html" or project == "css" or project == "web":
    language = "web"

elif project == "rs" or project == "rust":
    language = "rust"

elif project == "cpp" or project == "c++":
    language = "c++"

elif project == "go":
    language = "go"

elif project == "ts" or project == "typescript":
    language = "typescript"

elif project == "cs" or project == "c#":
    language = "c#"

elif project == "git" or project == "repos":
    language = "git"

else:
    print(
        dedent(
            f"""
    {bg.RED}ERR{bg.RESET} {fc.RESET}Unknown project type.
    
    Usage: {fc.CYAN}pycmd ls [language]{fc.RESET}
    
    See the list of projects below:
        
    {fc.LIGHTBLUE_EX}git{fc.LIGHTBLACK_EX}  -  {fc.GREEN}Github Repositories
    {fc.LIGHTBLUE_EX}py{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Python Project
    {fc.LIGHTBLUE_EX}js{fc.LIGHTBLACK_EX}   -  {fc.GREEN}JavaScript Project
    {fc.LIGHTBLUE_EX}java{fc.LIGHTBLACK_EX} -  {fc.GREEN}Java Project
    {fc.LIGHTBLUE_EX}html{fc.LIGHTBLACK_EX} -  {fc.GREEN}Web Project
    {fc.LIGHTBLUE_EX}rs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Rust Project
    {fc.LIGHTBLUE_EX}cpp{fc.LIGHTBLACK_EX}  -  {fc.GREEN}C++ Project
    {fc.LIGHTBLUE_EX}go{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Go Project
    {fc.LIGHTBLUE_EX}ts{fc.LIGHTBLACK_EX}   -  {fc.GREEN}TypeScript Project
    {fc.LIGHTBLUE_EX}cs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}C# Project
    """
        )
    )
    exit(1)

if language == "git":
    list_repos()
    print()
    exit()

with open("json/config.json", "r") as file:
    config = read(file)

try:
    projects_path = config["projects"][f"{language}_projects_path"]
except KeyError:
    print(
        bg.RED
        + "ERR"
        + bg.RESET
        + " "
        + f"{language.title()} Projects path is not specified."
    )
    print(
        bg.BLUE
        + "INFO"
        + bg.RESET
        + " "
        + f"Please add the path to the config.json file or run the {fc.CYAN}pycmd setup projects{fc.RESET} command.\n"
    )
    exit(1)
 
list_dir(projects_path)

print()