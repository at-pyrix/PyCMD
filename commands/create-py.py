import json
from time import sleep
from github import Github
import sys
import os
from colorama import Fore as fc

os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

def get_env(property):
    env_file = open(".env", "r")
    secrets = env_file.read()
    env_file.close()
    env_dict = {}
    for i in secrets.splitlines():
        key, value = i.split("=")
        env_dict[key] = value.replace('"', '').strip()
    return env_dict[property]


token = get_env("GITHUB_TOKEN")

with open("json/config.json", "r") as file:
    config = json.load(file)
    file.close()
    
python_projects_path = config['config']['python_projects_path']
project_name = sys.argv[1].replace('.py', '').strip()
_dir = os.path.join(python_projects_path, project_name)

g = Github(token)
user = g.get_user()
login = user.login


try:
    if len(sys.argv) == 3 and sys.argv[2] == 'p' or 'private':
        repo = user.create_repo(project_name, private=True)
    else:
        repo = user.create_repo(name=project_name, private=False)
except Exception as e:
    e = str(e)
    done = True
    if "name already exists" in e:
        print(fc.LIGHTRED_EX+"\r❌ " +
                "There is already another repository named"+project_name+fc.RESET)
        exit(1)
    else:
        print(fc.LIGHTRED_EX+"\r❌ "+e+"                "+fc.RESET)
        exit(1)

try:
    os.mkdir(_dir)
    os.chdir(_dir)
except FileExistsError:
    print(fc.LIGHTRED_EX + f"\r❌ A Project named '{project_name}' already exists"+fc.RESET)
    exit(1)

with open(f'Main.py', 'a+') as main_py:
    main_py.write('def main():\n\tpass\n\nif __name__ == \'__main__\':\n\tmain()')
    main_py.close()

with open("README.md", 'a+') as readme:
    readme.write(F'# {project_name.title()}')
    readme.close()

with open(".gitignore", 'a+') as gitignore:
    gitignore.write('*.pyc\n__pycache__\n.vscode\n.env\n')

commands = [
    'git init',
    f'git remote add origin https://github.com/{login}/{project_name}.git',
    'git add -A',
    'git commit -m "Initial commit"',
    'git push -u origin master'
]

print(fc.GREEN + "Initializing Git Repository..." + fc.RESET + "\n")
for c in commands:
    os.system(c)

print(f"\n\n✓ {fc.LIGHTGREEN_EX}Created A New Project: {fc.RESET}")
print(f"Opening with {fc.BLUE}Visual Studio Code")
os.system('code .')
