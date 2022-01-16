import sys
import os
from colorama import Fore as fc
from subprocess import getoutput
import threading
import itertools
import time
repo_Name = sys.argv[1].replace('.js', '').strip()
flags = sys.argv[1]

token = os.environ['github_token']
path = 'C:\\Programming\\Web_Projects'

def animate():
    for c in itertools.cycle(['⡿ Creating', '⣟ Creating', '⣯ Creating', '⣷ Creating', '⣾ Creating', '⣽ Creating', '⣻ Creating', '⢿ Creating']):
        if done:
            break
        sys.stdout.write('\r'+fc.LIGHTCYAN_EX+c)
        sys.stdout.flush()
        time.sleep(0.06)


done = False
t = threading.Thread(target=animate)

if len(sys.argv) == 3:
    if sys.argv[2] == "-p":
        from github import Github
        g = Github(token)
        user = g.get_user()
        login = user.login
        try:
            repo = user.create_repo(repo_Name, private=True)
        except Exception as e:
            e = str(e)

else:
    from github import Github
    g = Github(token)
    user = g.get_user()
    login = user.login
    try:
        repo = user.create_repo(repo_Name, private=False)
    except Exception as e:
        e = str(e)


if ".js" in flags:
    t.start()
    _dir = path+"\\Javascript\\"+repo_Name

    try:
        os.mkdir(_dir)
        os.chdir(_dir)
    except Exception as e:
        e = str(e)
        done = True

        if "file already exists" in e:
            print(fc.LIGHTRED_EX +
                  f"\r❌ A Project named '{repo_Name}' already exists"+fc.RESET)
            exit()
        else:
            print(fc.LIGHTRED_EX+"\r❌ "+str(e)+" "*20+fc.RESET)
            exit()

    with open("README.md", 'a+') as readme:
        readme.write(F'# {repo_Name.title()}\n\n #### Readme Auto Generated')
        readme.write('\n---')
        readme.close()
    with open('main.js', 'a+') as file:
        file.write('console.log("Hello, World!");')
        file.close()

    with open("desktop.ini", "w") as file:
        file.write("[.ShellClassInfo]\nIconResource=C:\\Programming\\ico\\git-folder-icon.ico,0\n[ViewState]\nMode=\nVid=\nFolderType=Generic")
        file.close()
        os.system("attrib +h +s +a desktop.ini")

    commands = [
        'git init',
        f'git remote add origin https://github.com/{login}/{repo_Name}.git',
        'git add -A',
        'git commit -m "Initial commit"',
        'git push -u origin master'
    ]

    for c in commands:
        getoutput(c)

    done = True
    print(f"\r{fc.LIGHTGREEN_EX}Created a new Javascript Project: {repo_Name.title()}{fc.RESET}")
    print(f"{fc.LIGHTGREEN_EX}Created New Github Repository: {repo_Name.title()}{fc.RESET}")
    os.chdir(_dir)
    os.system('code .')


else:
    t = threading.Thread(target=animate)
    t.start()
    _dir = path+"\\Websites\\"+repo_Name

    try:
        os.mkdir(_dir)
        os.chdir(_dir)
    except Exception as e:
        e = str(e)
        done = True

        if "file already exists" in e:
            print(fc.LIGHTRED_EX +
                  f"\r❌ A Project named '{repo_Name}' already exists"+fc.RESET)
            exit()
        else:
            print(fc.LIGHTRED_EX+"\r❌ "+str(e)+"                "+fc.RESET)
            exit()

    with open(f'index.html', 'a+') as file:
        file.write(
            f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{repo_Name}</title>\n\t<link rel="stylesheet" href="style.css">\n</head>\n<body>\n\n<script src="main.js"></script>\n</body>\n</html>\n'
        )

        file.close()
    with open(f'style.css', 'a+') as file:
        file.write("*{\n\t/*Auto Generated*/\n}")
        file.close()
    with open(f'main.js', 'a+') as file:
        file.write('alert("Hello World!");')
        file.close()

    with open("README.md", 'a+') as readme:
        readme.write(F'# {repo_Name.title()}\n\n #### Readme Auto Generated')
        readme.write('\n---')
        readme.close()

    with open("desktop.ini", "w") as file:
        file.write("[.ShellClassInfo]\nIconResource=C:\\Programming\\ico\\git-folder-icon.ico,0\n[ViewState]\nMode=\nVid=\nFolderType=Generic")
        file.close()
        os.system("attrib +h +s -a desktop.ini")

    commands = [
        'git init',
        f'git remote add origin https://github.com/{login}/{repo_Name}.git',
        'git add -A',
        'git commit -m "Initial commit"',
        'git push -u origin master'
    ]

    for c in commands:
        from subprocess import getoutput
        getoutput(c)

    done = True
    print(
        f"\r{fc.LIGHTGREEN_EX}Created a new Web Project: {repo_Name.title()}{fc.RESET}")
    print(f"{fc.LIGHTGREEN_EX}Created New Github Repository: {repo_Name.title()}{fc.RESET}")
    os.chdir(_dir)
    os.system('code .')
