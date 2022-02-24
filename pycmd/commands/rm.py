import os
from stat import S_IWRITE
import shutil
from json import load as read
from textwrap import dedent
from github import Github, GithubException
from github.GithubException import UnknownObjectException
from dotenv import load_dotenv, get_key
from pycmd.utils.pycmd import argparse
from colorama import Fore as fc, Back as bg, init

init(autoreset=True)

load_dotenv()
print()

project, flags = argparse()
git = False

bypass_prompt = True if "-y" in flags else False

token = get_key(".env", "GITHUB_TOKEN")

gh = Github(token)
user = gh.get_user()

language = ""
if project == ".":
    project = "untitled.unknown"
extension = project.split(".")[-1]
project = project.split('.')[0]

if extension == "py":
    language = "python"

elif extension == "js" or extension == "nodejs":
    language = "javascript"

elif extension == "java":
    language = "java"

elif extension == "html" or extension == "css" or extension == "web":
    language = "web"

elif extension == "rs":
    language = "rust"

elif extension == "cpp" or extension == "c++":
    language = "c++"

elif extension == "go":
    language = "go"

elif extension == "ts":
    language = "typescript"

elif extension == "cs":
    language = "c#"

elif extension == "git" or extension == "github":
    language = 'git'

else:
    print(
        dedent(
            f"""
    {bg.RED}ERR{bg.RESET} {fc.RESET}Unknown project type.
    
    Usage: {fc.CYAN}pycmd rm [project].[language]{fc.RESET}
    
    See the list of projects below:
        
    {fc.LIGHTBLUE_EX}.git{fc.LIGHTBLACK_EX}  -  {fc.GREEN}Github Repository
    {fc.LIGHTBLUE_EX}.py{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Python Project
    {fc.LIGHTBLUE_EX}.js{fc.LIGHTBLACK_EX}   -  {fc.GREEN}JavaScript Project
    {fc.LIGHTBLUE_EX}.java{fc.LIGHTBLACK_EX} -  {fc.GREEN}Java Project
    {fc.LIGHTBLUE_EX}.html{fc.LIGHTBLACK_EX} -  {fc.GREEN}Web Project
    {fc.LIGHTBLUE_EX}.rs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Rust Project
    {fc.LIGHTBLUE_EX}.cpp{fc.LIGHTBLACK_EX}  -  {fc.GREEN}C++ Project
    {fc.LIGHTBLUE_EX}.go{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Go Project
    {fc.LIGHTBLUE_EX}.ts{fc.LIGHTBLACK_EX}   -  {fc.GREEN}TypeScript Project
    {fc.LIGHTBLUE_EX}.cs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}C# Project
    """
        )
    )
    exit(1)


def on_rm_error(func, path, exc_info):
    os.chmod(path, S_IWRITE)
    os.unlink(path)

def delete_project(project_name):

    with open("json/config.json", "r") as file:
        config = read(file)

    try:
        root_folder = config["projects"][f"{language}_projects_path"]
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
        return

    if os.path.exists(f"{root_folder}/{project_name}"):
        print(
            f"{bg.LIGHTBLUE_EX}{fc.BLACK}CONFIRM{fc.RESET}{bg.RESET} "
            + f'This will delete all the contents of {fc.LIGHTBLACK_EX}"{fc.CYAN}{project}{fc.LIGHTBLACK_EX}"{fc.RESET} Are you sure? [y/N]'
        )

        if input(f"{fc.CYAN}» {fc.GREEN}").lower() != "y":
            return

        try:
            shutil.rmtree(f"{root_folder}/{project_name}")

        except PermissionError:
            print(bg.RED + "ERR" + bg.RESET + " " + "Project is currently in use\n")
            return
        
        except Exception as e:
            print(bg.RED + "ERR" + bg.RESET + " " + f"{str(e)}\n")
            return

        else:
            print(
                f'\n{fc.GREEN}Deleted {fc.LIGHTBLACK_EX}"{fc.CYAN}{project_name}{fc.LIGHTBLACK_EX}"{fc.RESET} locally.'
            )
    else:
        print(bg.RED + "ERR" + bg.RESET + " " + "Project does not exist\n")


def delete_git(project_name):
    try:
        repository = user.get_repo(project_name)
    except UnknownObjectException:
        print(f"{bg.RED}ERR{bg.RESET} Repository not found\n")
        return

    else:
        if not bypass_prompt:
            print(
                f"\n{bg.LIGHTBLUE_EX}{fc.BLACK}CONFIRM{fc.RESET}{bg.RESET} "
                + f'Are you sure you want to delete the repository {fc.LIGHTBLACK_EX}"{fc.CYAN}{project_name}{fc.LIGHTBLACK_EX}"{fc.RESET}? [y/N]'
            )
            if input(f"{fc.CYAN}» {fc.GREEN}").lower() != "y":
                return
        try:
            repository.delete()
        except GithubException as e:
            print(bg.RED + "ERR" + bg.RESET + " " + str(e))
            return
        else:
            print(
                f'\n{fc.GREEN}Deleted {fc.LIGHTBLACK_EX}"{fc.CYAN}{project_name}{fc.LIGHTBLACK_EX}"{fc.RESET} from GitHub.\n'
            )

if language == 'git':
    delete_git(project)
else:
    delete_project(project)
    delete_git(project)

print()
