# Command Handler
import os
import sys
import msvcrt
import json
from difflib import SequenceMatcher
from colorama import Fore as fc, Back as bk, Style as st, init
init(autoreset=True)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def help(command: str):
    file = open('json/commands.json', 'r')
    data = json.load(file)
    for i in data:
        if i['name'] == command:
            print(f'\n\nHelp for {fc.CYAN}{command}\n')
            print(
                f'{fc.LIGHTWHITE_EX}{i["description"]}\n\n')
            print(
                f'Usage{fc.BLACK}: {fc.YELLOW}{i["usage"]}\n')
            try:
                print(
                    f'Example{fc.BLACK}: {fc.LIGHTBLUE_EX}{i["example"]}\n')
                print(
                    f'Parameters{fc.BLACK}: {fc.GREEN}{", ".join(i["parameters"])}\n')
                print(
                    f'Flags{fc.BLACK}: {fc.LIGHTBLACK_EX}{i["flags"]}\n')
            except KeyError:
                pass


def autocorrect(word, word_list, tolerance=0.4):
    for filter_word in word_list:
        if SequenceMatcher(a=word, b=filter_word).ratio() > tolerance:
            return filter_word
    return None


def execute(function: str, parameter: str, flags: list):
    if "help" in flags:
        if function == "--help":
            os.system("python commands/help.py help " + " ".join(flags))
            return 0
        else:
            help(function)
            return 0

    if "help" in function:
        os.system("python commands/help.py help " + " ".join(flags))
        return 0

    if os.path.exists(f'commands/{function}.py'):
        os.system(
            f'python commands/{function}.py {parameter} {" ".join(flags)}')
        return 0
    else:
        corrected = autocorrect(function.lower(), os.listdir('commands'))
        if corrected:
            corrected = corrected.replace('.py', '')
            print(f'\nCommand {fc.LIGHTBLACK_EX}"{fc.LIGHTRED_EX}{function}{fc.LIGHTBLACK_EX}"{fc.RESET} not found.\nDid you mean {fc.LIGHTBLACK_EX}"{fc.CYAN}{corrected}{fc.RESET}{fc.LIGHTBLACK_EX}"{fc.RESET}?')
            print(
                f'{fc.LIGHTBLACK_EX}[{fc.GREEN}Y{fc.LIGHTBLACK_EX}/{fc.BLUE}n{fc.LIGHTBLACK_EX}]', end="\r")
            response = msvcrt.getch()
            if response.lower() == b'y':
                print(fc.LIGHTGREEN_EX + 'Yes  \n')
                execute(corrected, parameter, flags)
            else:
                print(fc.BLUE + 'Abort')
        else:
            print(f'\nCommand "{function}" not found.')
        return 1


if len(sys.argv) > 1:
    function = sys.argv[1] if len(sys.argv) > 1 else None
    parameter = sys.argv[2] if len(sys.argv) > 2 else "."
    flags = [
        f"{flag.replace('-', '')}" for flag in sys.argv if flag.startswith("-")]
    execute(function, parameter, flags)

else:
    os.system('python commands/help.py')
