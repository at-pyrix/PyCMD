from distutils.command.config import config
from colorama import Fore as fc, Style as st, init
import os
from sys import argv
import json
init(autoreset=True)

os.chdir(os.path.dirname(os.path.realpath(__file__ + "/..")))

colors = [fc.BLACK, fc.RED, fc.GREEN, fc.YELLOW, fc.BLUE, fc.MAGENTA, fc.CYAN, fc.WHITE,
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

__setup_done__ = config['$setup']

pc_name = os.environ['COMPUTERNAME']
user_name = os.getlogin()

color_enabled = True


setup = f"""
{fc.LIGHTCYAN_EX}Welcome to PYCMD!{fc.RESET}

{ascii_art}

PYCMD is a command line tool that helps you create and manage your projects.
It's {fc.LIGHTGREEN_EX}Free{fc.RESET} and {fc.LIGHTGREEN_EX}Open Source{fc.RESET}.

Github: {fc.LIGHTBLUE_EX}https://www.github.com/Yasho022/pycmd{fc.RESET}

{st.DIM}We'll walk you through the process of setting up your first project.{fc.RESET}{st.RESET_ALL}

{fc.LIGHTGREEN_EX}If that looks good to you, start by typing:
{fc.LIGHTRED_EX}$ {fc.YELLOW}pycmd {fc.RESET}setup{fc.RESET}
"""

if not __setup_done__ and not "help" in argv:
    print((setup))
else:
    print(ascii_art)

    print(f"""
{fc.LIGHTWHITE_EX}USAGE{fc.RESET}:

{fc.CYAN}# {user_name} {fc.LIGHTBLACK_EX}@{fc.LIGHTGREEN_EX} {pc_name} {fc.LIGHTBLACK_EX}in{fc.LIGHTYELLOW_EX} ~{fc.RESET}
{fc.RED}${fc.YELLOW} pycmd {fc.RESET} <command> {fc.GREEN}"<argument>"{fc.LIGHTBLACK_EX} <flags> {fc.RESET}
""")

    # TABLE OF COMMANDS
    file = open('json/commands.json', 'r')
    commands_data = json.load(file)

    print(fc.CYAN + "┌" + "─"*27 + "┬" + "─"*46 + "┐")
    print(f"{fc.CYAN}│{fc.YELLOW}{'Commands'.center(14, ' ')}{fc.CYAN}{' │'.center(25, ' ')}{fc.YELLOW}{'   Description'.center(15, ' ')}{fc.CYAN}{' '*20}│")

    print(fc.CYAN + "├" + "─"*27 + "┴" + "─"*46 + "┤")
    for i in commands_data:
        name_center = i['name'].center(15, ' ')
        space_for_dash_left = " "*12
        print(
            f"{fc.LIGHTBLACK_EX}│{fc.LIGHTBLUE_EX}{name_center}{space_for_dash_left}{fc.LIGHTBLACK_EX}:  {fc.GREEN}{i['description'].center(39, ' ')}     {fc.LIGHTBLACK_EX}│")
    print(fc.LIGHTBLACK_EX + "└" + "─"*74 + "┘")


    print("\nFor more information on a specific command, type:")
    print(f"{fc.LIGHTRED_EX}$ {fc.YELLOW}pycmd {fc.LIGHTBLUE_EX}<command>{fc.LIGHTBLACK_EX} --help")
########################
