# Command handler for the create command
from github import Github
from colorama import Fore as fc, Back as bg, init
from subprocess import run
import sys
import msvcrt
import json
import itertools
import textwrap
import os
from dotenv import load_dotenv
import threading
import re
import time
import cursor
init(autoreset=True)
load_dotenv()


def argparse(args: list):
    argument = ''
    flags = []
    for arg in args:
        if arg.startswith('-'):
            flags.append(arg)
        else:
            argument = arg
    return argument, flags


argument, flags = argparse(sys.argv)

# Making the characters variable-friendly with regex
# Source: https://stackoverflow.com/a/3305731

# This will send it to "Unknown Project"
if "." not in argument:
    argument = 'untitled.unknown'
project_name = re.sub('\W|^(?=\d)', '_', argument.split('.')[0])

with open("json/config.json", "r") as file:
    config = json.load(file)
    file.close()

extension = ''

if '.py' in argument:
    extension = '.py'
    language = 'python'
    root_folder = config['projects']['python_projects_path']
    boiler_plate = f"""
    # {project_name}
    
    def main():
        # Write your code here
        pass
        
    if __name__ == '__main__':
        main()
    """

elif '.js' in argument or '.nodejs' in argument:
    extension = '.js'
    language = 'javascript'
    root_folder = config['projects']['node.js_projects_path']
    boiler_plate = f"// {project_name}\n"

elif '.java' in argument:
    extension = '.java'
    language = 'java'
    root_folder = config['projects']['java_projects_path']
    boiler_plate = f"""
    // {project_name}
    
    import java.util.Scanner;
    
    class {project_name} {{
    
        public static void main(String[] args) {{
            
            Scanner scanner = new Scanner(System.in);
            
            // Write your code here
            
            scanner.close();
        }}
    }}   
    """

elif '.html' in argument or '.css' in argument or '.web' in argument:
    language = 'web'
    root_folder = config['projects']['web_projects_path']
    boiler_plate = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name}</title>
        <script src="index.js"></script>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <!-- Write your code here -->
    </body>
    </html>
    """

elif '.rs' in argument:
    extension = '.rs'
    language = 'rust'
    root_folder = config['projects']['rust_projects_path']

    boiler_plate = f"""
    // {project_name}
    
    fn main() {{
        // Write your code here
    }}
    """

elif '.cpp' in argument or '.c++' in argument:
    extension = '.cpp'
    language = 'c++'
    root_folder = config['projects']['cpp_projects_path']

    boiler_plate = f"""
    // {project_name}
    
    int main() {{
    // Write your code here
}}
    """

elif '.go' in argument:
    extension = '.go'
    language = 'go'
    root_folder = config['projects']['go_projects_path']

    boiler_plate = f"""
    // {project_name}
    
    package main
    
    func main() {{
        // Write your code here
    }}
    """

elif '.ts' in argument:
    extension = '.ts'
    language = 'typescript'
    root_folder = config['projects']['typescript_projects_path']
    boiler_plate = f"// {project_name}\n"

elif '.cs' in argument and not '.css' in argument:
    extension = '.cs'
    language = 'c#'
    root_folder = config['projects']['c#_projects_path']
    boiler_plate = f"""
    // {project_name}
    
    using System;
    
    class {project_name} {{    
        static void Main(string[] args)
        {{
            // Write your code here
        }}
    }}
    """

else:
    print('Unknown Project')
    exit(1)


end = False
text = ''

# Inspired from: https://stackoverflow.com/a/22029635


def animate():
    cursor.hide()
    for c in itertools.cycle(['⠟', '⠯', '⠷', '⠾', '⠽', '⠻']):
        if end:
            break
        sys.stdout.write("\r" + fc.LIGHTYELLOW_EX +
                         c + fc.RESET + f' {text}')
        sys.stdout.flush()
        time.sleep(0.07)
    cursor.show()


def git_init(name, private: bool = False):

    load_anim = threading.Thread(target=animate)
    load_anim.daemon = True

    token = os.environ.get('GITHUB_TOKEN')

    gh = Github(token)
    user = gh.get_user()
    public_priv = 'private' if private else 'public'

    print(
        f'\n{fc.MAGENTA}Initializing {public_priv} repository: {fc.LIGHTYELLOW_EX}{name}')

    global text, end
    text = 'Creating repository'

    load_anim.start()
    try:
        user.create_repo(name, private=private)
        commands = [{'cd ' + project_path: 'Changing directory to ' + os.path.relpath(project_path)},
                    {'git init': 'Initializing git repository'},
                    {f'git remote add origin https://github.com/{user.login}/{project_name}.git': 'Connecting to remote repository'},
                    {'git add -A': 'Adding files'},
                    {'git commit -m "Initial commit"': 'Committing files'},
                    {'git push -u origin master': 'Pushing files to remote'}
                    ]
    except Exception as e:
        end = True
        e = '{' + str(e).split('{')[1].split('}')[0] + '}'
        err_message = json.loads(e.replace("'", '"'))['message']
        print(bg.RED + '\rERR' + bg.RESET + " " + err_message + " " * 20)
        exit(1)
    else:
        for i in commands:
            command = list(i.keys())[0]
            description = i[command]
            output = run(command, shell=True, capture_output=True)
            if output.returncode == 0:
                text = description + ' ' * 20
                time.sleep(.3)
            else:
                end = True
                print(bg.RED + '\rERR' + bg.RESET +
                      " " + f'An error occurred while {description.lower()}' + " " * 20)
                print(bg.BLUE + fc.BLACK + 'INFO' + fc.RESET + bg.RESET + ' ' +
                      f'While executing: {fc.CYAN}"' + command + f'"{fc.RESET}: \n')
                print(output.stderr.decode('unicode_escape'))
                exit(1)
        end = True
        load_anim.join()
        print(fc.GREEN + '\rSuccessfully initialized git' + ' ' * 20)


boiler_plate = textwrap.dedent(boiler_plate).strip()


# If you want to never get this warning, change this line to:

"""
Original: `if '-y' not in flags:`

Modified: `if False:`

"""
if '-y' not in flags:

    def listen_to_keyboard():
        while not time_over:
            key = msvcrt.getch()
            if key == b'n':
                global cancelled
                print(fc.RED + '\rCancelled' + ' ' * 20)
                cancelled = True
                break
            elif key == b'y':
                global continued
                print("\r" + fc.YELLOW + "\rCreating project in " +
                      project_path)
                continued = True
                break

    print(fc.LIGHTBLACK_EX +
          "\nYou can skip this delay by passing the '-y' flag. Example: pycmd create test.py -y")
    print(
        f"Press {fc.LIGHTWHITE_EX}'Y'{fc.RESET} to continue or {fc.LIGHTWHITE_EX}'N'{fc.RESET} to cancel.")
    cancelled = False
    time_over = False
    continued = False
    threading.Thread(target=listen_to_keyboard).start()
    for i in range(5, 0, -1):
        if cancelled:
            exit(0)
        if continued:
            break
        sys.stdout.write(f'\rCreating project in {fc.CYAN}{i}{fc.RESET}...')
        time.sleep(1)
    time_over = True

print(fc.MAGENTA + '\nGenerating boiler plate...')

project_path = os.path.join(root_folder, project_name)

try:
    os.mkdir(project_path)
    os.chdir(project_path)
except Exception as e:
    print(bg.RED + '\rERR' + bg.RESET + " " + str(e).split('] ')[1] + " " * 20)
    exit(1)

if language == 'web':
    with open('index.html', 'w') as file:
        file.write(boiler_plate)
        file.close()
    open('index.js', 'w').close()
    open('style.css', 'w').close()

elif language == 'javascript':
    with open(f'index.js', 'w') as file:
        file.write(boiler_plate)
        file.close()

    
    output = run(f'npm init -y', shell=True, capture_output=True)
    if output.returncode != 0:
        print(bg.RED + '\rERR' + bg.RESET +
            " " + 'While initializing npm' + " " * 20)
        print(bg.BLUE + fc.BLACK + 'INFO' + fc.RESET + bg.RESET + ' ' +
            f'While executing: {fc.CYAN}"' + 'npm init -y' + f'"{fc.RESET}: \n')
        print(output.stderr.decode('unicode_escape'))
        print('\nSkipping...')

else:
    with open('index' + extension, 'w') as file:
        file.write(boiler_plate)
        file.close()

with open('README.MD', 'w') as file:
    file.write('# ' + project_name)
    file.close()

print(fc.GREEN + 'Successfully generated boiler plate')

if not '-local' in flags and not '-l' in flags:
    if '-private' in flags or '-p' in flags:
        git_init(project_name, True)
    else:
        git_init(project_name)

# Open project

if config['text-editor'] == 'Visual Studio Code':
    os.system(f'code {project_path}')
elif config['text-editor'] == 'Vim':
    os.system(f'vim {project_path}')
elif config['text-editor'] == 'Sublime Text':
    os.system(f'subl {project_path}')
elif config['text-editor'] == 'Atom':
    os.system(f'atom {project_path}')
elif config['text-editor'] == 'Emacs':
    os.system(f'emacs {project_path}')
elif config['text-editor'] == 'Nano':
    os.system(f'nano {project_path}')