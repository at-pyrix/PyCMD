# Command Handler
import os
import sys
import msvcrt
import json
from difflib import SequenceMatcher
from colorama import Fore as fc, init
init(autoreset=True)

version = "1.0"

os.chdir(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def argparse(args: list):
    function = args[1] if not args[1].startswith('-') else ""
    parameter = ""
    flags = []
    for i in args[1:]:
        if i.startswith("--"):
            flags.append(i[1:])
        elif i.startswith("-"):
            flags.append(i)
        else:
            parameter = i if i != function else "."
        args.pop(args.index(i))

    return function, parameter, flags


def help(command: str):
    file = open('json/commands.json', 'r')
    data = json.load(file)
    for i in data:
        if i['name'] == command:
            if 'description' in i:
                print(" "*(2) +
                      f'\n{fc.YELLOW}{i["description"]}\n')
            if 'usage' in i:
                print(" "*(2) +
                      f'{fc.GREEN}Usage:' + " "*(15 - len('Usage:')) + f'{fc.RESET}{i["usage"]}')
            if 'parameters' in i:
                print(" "*(2) +
                      f'{fc.GREEN}Parameters:' + " "*(15 - len('Parameters:')) + f'{fc.RESET}{", ".join(i["parameters"])}')
            if 'flags' in i:
                print(" "*(2) +
                      f'{fc.GREEN}Flags:' + " "*(15 - len('Flags:')) + f'{fc.RESET}{i["flags"]}')
            if 'example' in i:
                print(" "*(2) +
                      f'{fc.GREEN}Example:' + " "*(15 - len('Example:')) + f'{fc.RESET}{i["example"]}')


def autocorrect(word, word_list, tolerance=0.4):
    for filter_word in word_list:
        if SequenceMatcher(a=word, b=filter_word).ratio() > tolerance:
            return filter_word
    return None


def execute(command: str, parameter: str, flags: list):
    # TODO: FIX THIS

    if not command:
        if "-v" in flags or "-version" in flags:
            print(f'PYCMD v{version}')
            return 0
        os.system("python commands/help.py help " + " ".join(flags))
        return 0

    if "-help" in flags or "-h" in flags:
        help(command)
        return 0
    
    elif command == "help":
        if parameter != ".":
            help(parameter)
        else:
            os.system('python commands/help.py')
        return 0

    if os.path.exists(f'commands/{command}.py'):
        os.system(
            f'python commands/{command}.py {parameter} {" ".join(flags)}')
        return 0
    else:
        corrected = autocorrect(command.lower(), os.listdir('commands'))
        if corrected:
            corrected = corrected.replace('.py', '')
            print(f'\nCommand {fc.LIGHTBLACK_EX}"{command}{fc.LIGHTBLACK_EX}"{fc.RESET} not found.\nDid you mean {fc.LIGHTBLACK_EX}"{fc.CYAN}{corrected}{fc.RESET}{fc.LIGHTBLACK_EX}"{fc.RESET}?')
            print(
                f'{fc.LIGHTBLACK_EX}[{fc.GREEN}Y{fc.LIGHTBLACK_EX}/{fc.BLUE}n{fc.LIGHTBLACK_EX}]', end="\r")
            response = msvcrt.getch()
            if response.lower() == b'y':
                print(fc.LIGHTGREEN_EX + 'Yes  \n')
                execute(corrected, parameter, flags)
            else:
                print(
                    f'Run {fc.CYAN}pycmd help{fc.RESET} for list of commands.')
        else:
            print(
                f'\nCommand {fc.LIGHTBLACK_EX}"{command}{fc.LIGHTBLACK_EX}"{fc.RESET} not found.')
            print(f'Run {fc.CYAN}pycmd help{fc.RESET} for list of commands.')
        return 1


if len(sys.argv) > 1:
    function, parameter, flags = argparse(sys.argv)
    try:
        execute(function, parameter, flags)
    except KeyboardInterrupt:
        pass

else:
    os.system('python commands/help.py')
