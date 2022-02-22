from github import Github
import requests
import sys
import dotenv
import os
from colorama import Fore as fc
import time
import sys
dotenv.load_dotenv(".env")

# TODO: Check if the project is a git repo by checking the .git folder

# checks if it is a file or a folder and lists the folder

def listdir(path):
    listdir_path = os.listdir(path)
    dir__ = []
    for file in listdir_path:
        filename, file_extension = os.path.splitext(file)
        file_extension = str(file_extension)
        if file_extension:
            continue
        else:
            dir__.append(filename)
    return dir__


if "repo" in sys.argv[1] or "git" in sys.argv[1]:
    g = Github(os.getenv('GITHUB_TOKEN'))
    user = g.get_user()
    login = user.login

    link = ('https://api.github.com/users/Yasho022/repos')

    try:
        api_link = requests.get(link)
        api_data = api_link.json()

    except:
        print(f"{fc.LIGHTRED_EX}An Error Occurred{fc.RESET}")

    repos_Data = (api_data)

    repos = []

    repos_pub = []
    repos_priv = []

    for item in repos_Data:
        try:
            repo_pub = item['name']
        except TypeError:
            print(f"{fc.LIGHTRED_EX}Max Limit Reached For API Calls{fc.RESET}")
            exit()
        else:
            repos_pub.append(repo_pub)

    for repo in g.get_user().get_repos():
        repo_priv = repo.name
        repos_priv.append(repo_priv)

    repos_pub = (sorted(repos_pub))
    repos_priv = (sorted(repos_priv))

    repositories = repos_pub
    repos_pub.extend(repos_priv)

    repos_priv = (set([x for x in repositories if repositories.count(x) == 1]))
    repos_pub = (set([x for x in repositories if repositories.count(x) > 1]))

    print(
        f"\r{fc.LIGHTGREEN_EX}Your Github Repositories {fc.LIGHTYELLOW_EX}[Total: {len(repos_Data)}]:{fc.RESET}\n")
    time.sleep(0.5)

    for repo in repos_pub:
        time.sleep(0.1)
        print(fc.LIGHTBLACK_EX+"• "+fc.RESET+repo)
    for repo in repos_priv:
        time.sleep(0.1)
        print(f"{fc.LIGHTBLACK_EX}• {fc.LIGHTBLACK_EX}{repo}{fc.RESET} ")

    print(fc.RESET)

elif "py" in sys.argv[1]:
    list_py = listdir('C:\\Programming\\Python_Projects')
    if list_py:
        print(
            f"{fc.LIGHTGREEN_EX}You have the following Python Projects{fc.LIGHTYELLOW_EX} [Total: {len(list_py)}]{fc.LIGHTWHITE_EX}\n")
        for item in list_py:
            root = listdir('C:\\Programming\\Python_Projects\\' + item)
            time.sleep(0.1)

            if ".git" in root:
                print(f"{fc.LIGHTBLACK_EX}• {fc.LIGHTGREEN_EX}{item}{fc.RESET}")
            else:
                print(fc.LIGHTBLACK_EX+"• " + fc.RESET + item + fc.RESET)
    else:
        print(
            f"{fc.LIGHTRED_EX}You have no Python Projects currently{fc.LIGHTWHITE_EX}")
    print(fc.RESET)


elif sys.argv[1] == "js" or "javascript" in sys.argv[1]:
    list_js = listdir('C:\\Programming\\Web_Projects\\Javascript\\')
    if list_js:
        print(
            f"{fc.LIGHTGREEN_EX}You have the following JavaScript Projects{fc.LIGHTYELLOW_EX} [Total: {len(list_js)}]{fc.LIGHTWHITE_EX}\n")
        for item in list_js:
            root = listdir(
                'C:\\Programming\\Web_Projects\\Javascript\\' + item)
            time.sleep(0.1)

            if ".git" in root:
                print(f"{fc.LIGHTBLACK_EX}• {fc.LIGHTGREEN_EX}{item}{fc.RESET}")
            else:
                print(fc.LIGHTBLACK_EX+"• " + fc.RESET + item + fc.RESET)
    else:
        print(
            f"{fc.LIGHTRED_EX}You have no Javascript Projects currently{fc.LIGHTWHITE_EX}")
    print(fc.RESET)

elif "java" in sys.argv[1]:
    list_java = listdir('C:\\Programming\\Java_Projects')
    if list_java:
        print(
            f"{fc.LIGHTGREEN_EX}You have the following Java Projects{fc.LIGHTYELLOW_EX} [Total: {len(list_java)}]{fc.LIGHTWHITE_EX}\n")
        time.sleep(0.5)
        for items in list_java:
            time.sleep(0.1)
            print(fc.LIGHTBLACK_EX+"• "+fc.RESET + items)
    else:
        print(
            f"{fc.LIGHTGREEN_EX}You have no Java Projects currently{fc.LIGHTWHITE_EX}")
    print(fc.RESET)

elif "web" in sys.argv[1] or "html" in sys.argv[1]:
    list_web = listdir('C:\\Programming\\Web_Projects\\Websites\\')
    if list_web:
        print(
            f"{fc.LIGHTGREEN_EX}You have the following Web Projects {fc.LIGHTYELLOW_EX}[Total: {len(list_web)}]{fc.LIGHTWHITE_EX}\n")
        time.sleep(0.5)
        for item in list_web:
            root = listdir('C:\\Programming\\Web_Projects\\Websites\\' + item)
            time.sleep(0.1)

            if ".git" in root:
                print(f"{fc.LIGHTBLACK_EX}• {fc.LIGHTGREEN_EX}{item}{fc.RESET}")
            else:
                print(fc.LIGHTBLACK_EX+"• " + fc.RESET + item + fc.RESET)
    else:
        print(f"{fc.LIGHTRED_EX}You have no Web Projects currently{fc.LIGHTWHITE_EX}")
    print(fc.RESET)

else:
    print(
        f"""{fc.LIGHTRED_EX}
See the List Arguments: [repo/py/js/java/web]\n{fc.RESET}
{fc.LIGHTBLACK_EX}• {fc.LIGHTYELLOW_EX}repo  {fc.LIGHTBLACK_EX}:  {fc.RESET}List {fc.LIGHTGREEN_EX}GitHub Repositories{fc.RESET}
{fc.LIGHTBLACK_EX}• {fc.LIGHTYELLOW_EX}py    {fc.LIGHTBLACK_EX}:  {fc.RESET}List {fc.LIGHTGREEN_EX}Python Projects {fc.RESET}
{fc.LIGHTBLACK_EX}• {fc.LIGHTYELLOW_EX}java  {fc.LIGHTBLACK_EX}:  {fc.RESET}List {fc.LIGHTGREEN_EX}Java Projects {fc.RESET}
{fc.LIGHTBLACK_EX}• {fc.LIGHTYELLOW_EX}js    {fc.LIGHTBLACK_EX}:  {fc.RESET}List {fc.LIGHTGREEN_EX}JavaScript Projects {fc.RESET}
{fc.LIGHTBLACK_EX}• {fc.LIGHTYELLOW_EX}web   {fc.LIGHTBLACK_EX}:  {fc.RESET}List {fc.LIGHTGREEN_EX}Web Projects (html/css){fc.RESET}
            """)
