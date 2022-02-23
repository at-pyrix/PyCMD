import json
import sys
import os
from textwrap import dedent
import re
from colorama import Fore as fc, Back as bg, Style as st, init
init(autoreset=True)

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

if "." not in argument:
    argument = 'untitled.unknown'
project_name = re.sub('\W|^(?=\d)', '_', argument.split('.')[0])

if '.py' in argument:
    language = 'python'

elif '.js' in argument or '.nodejs' in argument:
    language = 'javascript'

elif '.java' in argument:
    language = 'java'

elif '.html' in argument or '.css' in argument or '.web' in argument:
    language = 'web'

elif '.rs' in argument:
    language = 'rust'

elif '.cpp' in argument or '.c++' in argument:
    language = 'c++'

elif '.go' in argument:
    language = 'go'

elif '.ts' in argument:
    language = 'typescript'

elif '.cs' in argument and not '.css' in argument:
    language = 'c#'

else:
    print(dedent(f"""
    {bg.RED}ERR{bg.RESET} {fc.RESET}Unknown project type.
    See the list of projects below:
    
    {fc.LIGHTBLUE_EX}.py{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Python Project
    {fc.LIGHTBLUE_EX}.js{fc.LIGHTBLACK_EX}   -  {fc.GREEN}JavaScript Project
    {fc.LIGHTBLUE_EX}.java{fc.LIGHTBLACK_EX} -  {fc.GREEN}Java Project
    {fc.LIGHTBLUE_EX}.html{fc.LIGHTBLACK_EX} -  {fc.GREEN}Web Project
    {fc.LIGHTBLUE_EX}.rs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Rust Project
    {fc.LIGHTBLUE_EX}.cpp{fc.LIGHTBLACK_EX}  -  {fc.GREEN}C++ Project
    {fc.LIGHTBLUE_EX}.go{fc.LIGHTBLACK_EX}   -  {fc.GREEN}Go Project
    {fc.LIGHTBLUE_EX}.ts{fc.LIGHTBLACK_EX}   -  {fc.GREEN}TypeScript Project
    {fc.LIGHTBLUE_EX}.cs{fc.LIGHTBLACK_EX}   -  {fc.GREEN}C# Project
    """))
    exit(1)
    
with open('json/config.json') as config_file:
    config = json.load(config_file)
    
try:
    root_folder = config['projects'][f'{language}_projects_path']
except KeyError:
    print(bg.RED + 'ERR' + bg.RESET + " " + F'{language.title()} Projects path is not specified.')
    print(bg.BLUE + 'INFO' + bg.RESET + " " + F'Please add the path to the config.json file or run the {fc.CYAN}pycmd setup projects{fc.RESET} command.')
    exit(1)

project_path = os.path.join(root_folder, project_name)

try:
    editor = config['text-editor']
except KeyError:
    print(bg.RED  + 'ERR' +  bg.RESET + " " + 'No text editor specified in config.json')
    print(f'Set the default text editor to open the project with the {fc.CYAN}pycmd setup editor{fc.RESET} command.')
    exit()

if not os.path.exists(project_path): 
    print(fc.RED + 'Project not found')
    exit(1)

if '-e' in flags :
    print(fc.GREEN + f'Opening {project_name} with explorer...')
    os.system(f'explorer {project_path}')

else:
    
    print(fc.GREEN + f'Opening {project_name} with {editor}...')
    
if editor == 'Visual Studio Code':
    os.system(f'code {project_path}')
elif editor == 'Sublime Text':
    os.system(f'subl {project_path}')
elif editor == 'Atom':
    os.system(f'atom {project_path}')
else:
    os.system(f'cd {project_path} && {editor}')