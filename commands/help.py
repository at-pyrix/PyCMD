from distutils.command.config import config
from colorama import Fore as fc, Style as st, init
import os
from sys import argv
import json
init(autoreset=True)

os.chdir(os.path.dirname(os.path.realpath(__file__ + "/..")))

colors = [fc.LIGHTBLACK_EX, fc.RED, fc.GREEN, fc.YELLOW, fc.BLUE, fc.MAGENTA, fc.CYAN, fc.WHITE,
          fc.RESET,
          fc.LIGHTBLACK_EX, fc.LIGHTRED_EX, fc.LIGHTGREEN_EX, fc.LIGHTYELLOW_EX, fc.LIGHTBLUE_EX, fc.LIGHTMAGENTA_EX, fc.LIGHTCYAN_EX, fc.LIGHTWHITE_EX
          ]

ascii_art = (f"""

{fc.LIGHTMAGENTA_EX}d8888b.  db    db {fc.LIGHTRED_EX}  .o88b.  .88b   d8.   d8888b. 
{fc.LIGHTMAGENTA_EX}88  `8D  `8b  d8' {fc.LIGHTRED_EX}d8P  Y8   88'YbdP`88   88  `8D
{fc.LIGHTMAGENTA_EX}88oodD'   `8bd8'  {fc.LIGHTRED_EX}8P        88  88  88   88   88
{fc.LIGHTMAGENTA_EX}88~~"       88    {fc.LIGHTRED_EX}8b        88  88  88   88   88 
{fc.LIGHTMAGENTA_EX}88          88    {fc.LIGHTRED_EX}Y8b  d8   88  88  88   88  .8D 
{fc.LIGHTMAGENTA_EX}88          YP    {fc.LIGHTRED_EX} `Y88P'   YP  YP  YP   Y8888D'{fc.RESET}
""")

with open('json/config.json', 'r') as f:
    config = json.load(f)
    f.close()

__setup_done__ = config['is_setup']


setup = f"""
{fc.LIGHTCYAN_EX}Welcome to PYCMD!{fc.RESET}

{ascii_art}

PYCMD is a command line tool that helps you create and manage your projects.
It's {fc.LIGHTGREEN_EX}Free{fc.RESET} and {fc.LIGHTGREEN_EX}Open Source{fc.RESET}.

Github: {fc.LIGHTBLUE_EX}https://www.github.com/Yasho022/pycmd{fc.RESET}

{st.DIM}We'll walk you through the process of setting up PYCMD environment.{fc.RESET}{st.RESET_ALL}

{fc.LIGHTGREEN_EX}If that looks good to you, start by typing:
{fc.LIGHTRED_EX}$ {fc.YELLOW}pycmd {fc.RESET}setup{fc.RESET}
"""

if not __setup_done__ and not "help" in argv:
    print((setup))
    exit(0)


# And that's how you save one level of indentation.

print(ascii_art)

print(f"""
{fc.LIGHTWHITE_EX}USAGE{fc.RESET}:

{fc.RED}${fc.YELLOW} pycmd {fc.LIGHTBLUE_EX} <command> {fc.GREEN}<argument>{fc.LIGHTBLACK_EX} <flags> {fc.RESET}
""")

file = open('json/commands.json', 'r')
commands_data = json.load(file)

print(fc.CYAN + "┌" + "─"*28 + "┬" + "─"*45 + "┐")
print(f"{fc.CYAN}│{fc.YELLOW}{'Commands'.center(28, ' ')}{fc.CYAN}│{fc.YELLOW}{'Description'.center(42, ' ')}{fc.CYAN}{' '*3}│")

print(fc.CYAN + "└" + "─"*28 + "┴" + "─"*45 + "┘")

"""
┌────────────────────────────┬─────────────────────────────────────────────┐
│          Commands          │               Description                   │
└────────────────────────────┴─────────────────────────────────────────────┘
"""

print(fc.LIGHTBLACK_EX + "┌" + "─"*28 + "┬" + "─"*45 + "┐")
for i in commands_data:
    name_center = i['name'].center(27, ' ')
    description_center = i['description'].center(39, ' ')
    print(
        f"{fc.LIGHTBLACK_EX}│{fc.LIGHTBLUE_EX}{name_center} {fc.LIGHTBLACK_EX}│  {fc.GREEN}{description_center}    {fc.LIGHTBLACK_EX}│")
print(fc.LIGHTBLACK_EX + "└" + "─"*28 + "┴" + "─"*45 + "┘")

"""
┌────────────────────────────┬─────────────────────────────────────────────┐
│           command1         │                description1                 │
│           command2         │                description2                 │
│           command3         │                description3                 │
│           command4         │                description4                 │
│           command5         │                description5                 │
│           command6         │                description6                 │
│           command7         │                description7                 │
│           command8         │                description8                 │
└────────────────────────────┴─────────────────────────────────────────────┘
"""

print("\nFor more information on a specific command, type:")
print(f"{fc.LIGHTRED_EX}$ {fc.YELLOW}pycmd {fc.LIGHTBLUE_EX}<command>{fc.LIGHTBLACK_EX} --help")
