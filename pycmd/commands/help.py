from ast import Pass
from distutils.command.config import config
from colorama import Fore as fc, Style as st, init
import os
from sys import argv
import json
init(autoreset=True)

os.chdir(os.path.dirname(os.path.realpath(__file__ + "/..")))

ascii_art = (f"""{fc.LIGHTMAGENTA_EX}
d8888b.  db    db   .o88b.  .88b   d8.   d8888b. 
88  `8D  `8b  d8' d8P  Y8   88'YbdP`88   88  `8D
88oodD'   `8bd8'  8P        88  88  88   88   88
88~~"       88    8b        88  88  88   88   88 
88          88    Y8b  d8   88  88  88   88  .8D 
88          YP     `Y88P'   YP  YP  YP   Y8888D'
""")

try:
    with open('json/config.json', 'r') as f:
        config = json.load(f)
        f.close()
except FileNotFoundError:
    config = {'is_setup': False}

is_setup = config['is_setup']


setup = f"""
{fc.LIGHTCYAN_EX}Welcome to PYCMD!{fc.RESET}

{ascii_art}{fc.RESET}

PYCMD is a command line tool that helps you create and manage your projects.
It's {fc.LIGHTGREEN_EX}Free{fc.RESET} and {fc.LIGHTGREEN_EX}Open Source{fc.RESET}.

Github: {fc.LIGHTBLUE_EX}https://www.github.com/Yasho022/pycmd{fc.RESET}

{st.DIM}We'll walk you through the process of setting up PYCMD environment.{fc.RESET}{st.RESET_ALL}

{fc.LIGHTGREEN_EX}If that looks good to you, start by typing:
{fc.LIGHTBLACK_EX}$ {fc.BLUE}pycmd {fc.RESET}setup{fc.RESET}
"""

if not is_setup and not "-help" in argv:
    print(setup)
    exit(0)


# And that's how you save one level of indentation.

print(f"""
{fc.CYAN}USAGE

{fc.LIGHTBLACK_EX}${fc.GREEN} pycmd{fc.LIGHTBLUE_EX} <command>{fc.GREEN} <argument>{fc.LIGHTBLACK_EX} <flags> {fc.RESET}
""")

file = open('json/commands.json', 'r')
commands_data = json.load(file)

print(fc.CYAN + '\nCOMMANDS\n')

print(fc.LIGHTBLACK_EX + "┌" + "─"*28 + "┬" + "─"*45 + "┐")

for c, i in enumerate(commands_data):
    name_center = i['name'].center(27, ' ')
    description_center = i['description'].center(39, ' ')
    print(
        f"{fc.LIGHTBLACK_EX}│{fc.YELLOW}{name_center} {fc.LIGHTBLACK_EX}│  {fc.LIGHTMAGENTA_EX}{description_center}    {fc.LIGHTBLACK_EX}│")
    
    if c == len(commands_data) - 1:
        print(fc.LIGHTBLACK_EX + "└" + "─"*28 + "┴" + "─"*45 + "┘")
    else:
        print(fc.LIGHTBLACK_EX + "├" + "─"*28 + "┼" + "─"*45 + "┤")

print("\nFor more information on a specific command, type:")
print(f"{fc.LIGHTBLACK_EX}${fc.GREEN} pycmd{fc.LIGHTBLUE_EX} help {fc.GREEN}<command>")
