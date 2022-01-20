from colorama import Fore as fc, Back as bk, Style as st, init
import wx
from difflib import SequenceMatcher
import msvcrt
from time import sleep
import sys
import os
import json
init(autoreset=True)


def autocorrect(word, word_list, tolerance=0.4):
    for filter_word in word_list:
        if SequenceMatcher(a=word, b=filter_word).ratio() > tolerance:
            return filter_word
    return None


def get_path():
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.DirDialog(None, 'Open', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


def getpass(prompt=''):
    p_s = ''
    proxy_string = ['​'] * 40
    while True:
        sys.stdout.write('\x0D' + prompt + ''.join(proxy_string))
        c = msvcrt.getch()
        if c == b'\r':
            break
        elif c == b'\x08':
            p_s = p_s[:-1]
            proxy_string[len(p_s)] = " "
        else:
            proxy_string[len(p_s)] = "*"
            p_s += c.decode()

    sys.stdout.write('\n')
    return p_s


print(f"\n\n{fc.CYAN}PYCMD Setup")

print("""
This script will help you to setup your PYCMD environment.
It saves your configuration in "config.json" in the json directory. 

After you have finished the setup, run `pycmd --help`
to get the list of commands and usage.    

You can change these settings anytime.

""")

print("── Press any key to continue ──", end="")
msvcrt.getch()


print("\r" + fc.LIGHTWHITE_EX + "Which programming language do you work with?")
print(fc.LIGHTBLACK_EX + "Seperate multiple answers with a comma (,)\n")

languages_supported = ['Python', 'C++',
                       'C#', 'Java', 'Go', 'Rust', 'Node.js', 'TypeScript', 'Web (HTML, CSS, JS)', 'Other']


for i in languages_supported:
    print(f"{fc.BLACK}•{fc.LIGHTBLUE_EX} {i}")
    sleep(0.1)
print()


languages_wanted = [i.lower().strip() for i in input(
    fc.CYAN + "» " + fc.GREEN).split(",")]
print(fc.RESET)

languages_got = []

for lang in languages_wanted:
    i = autocorrect(lang, languages_supported)

    # Abbreviations
    if lang == 'css' or lang == 'html' or lang == 'web':
        i = 'Web (HTML, CSS, JS)'
    if lang == 'js' or lang == 'javascript':
        i = 'Web (HTML, CSS, JS)'
    if lang == 'ts' or lang == 'typescript':
        i = 'TypeScript'
    if lang == 'py' or lang == 'python':
        i = 'Python'
    if lang == 'go' or lang == 'golang':
        i = 'Go'

    if i in languages_supported:
        languages_got.append(i)

if languages_got == ['Other']:
    print("\r" + fc.LIGHTWHITE_EX + "What programming language do you work with?")
    selection = input(fc.CYAN + "» " + fc.GREEN)
    languages_got = [selection]

if not languages_got:
    print(fc.LIGHTRED_EX + "Whoops!")
    print("Looks like we don't support any of those languages.")
    print("Here, have a cookie: 🍪\n")
    print('You can help us by adding it to the list of supported languages.')
    print(f'{fc.BLUE}https://www.github.com/Yasho022/pycmd/issues/new')
    exit(1)

else:
    del languages_supported
    print(fc.GREEN + ', '.join(languages_got))

config = {"is_setup": True, "projects": {}}

print(fc.LIGHTWHITE_EX + "\nDo you organize your projects in folders? (Y/n)")
response = input(fc.CYAN + "» " + fc.RESET).lower()
if response == "y" or response == "yes":
    print(fc.GREEN + "\nAwesome! Let's set up your project folders.")
    print(fc.BLACK + "─" * 58)
    print(fc.BLACK + "Select the folder from the popup\n(maybe it's already open but not in focus)")

    try:
        for i in languages_got:
            if "Web" in i:
                i = "Web"
            print(fc.LIGHTWHITE_EX +
                  f"\nWhere do you save all your {i} projects?")
            print(fc.CYAN + "» " + fc.GREEN, end="\r")
            path = get_path()
            print(fc.CYAN + "» " + fc.GREEN + path)
            if i == "HTML + CSS":
                i = "web"
            config['projects'][f'{i.lower()}_projects_path'] = path
    except:
        print(st.DIM + fc.CYAN + "» " + st.RESET_ALL +
              fc.RED + "You didn't select a folder :/")
        exit(1)

else:
    print("\nWe got you covered! We'll create the folders for you.")
    print(fc.BLACK + "Select the folder from the popup\n(maybe it's already open but not in focus)")
    print(fc.LIGHTWHITE_EX +
          "\nAlright, just tell us your root folder where you save all your projects.")
    print(fc.CYAN + "» " + fc.GREEN, end="\r")
    root_folder = get_path()

    if root_folder is None:
        print(fc.CYAN + "» " + fc.RED + "No folder selected :/")
        print(fc.GREEN + "\nNevermind, we'll do that too. We'll just use the PYCMD/Projects directory.")
        print(fc.LIGHTWHITE_EX +
              "\nIf you're okay with that, press [Y] to continue.")
        key = msvcrt.getch()
        if key.lower() == b'y':
            os.mkdir('Projects')
            root_folder = os.path.abspath('Projects')
        else:
            print(fc.RED + "Sorry, we can't continue without a root folder.")
            exit(1)

    print(fc.CYAN + "» " + fc.GREEN + root_folder)
    print()
    for i in languages_got:
        if "Web" in i:
            i = "Web"
        folder = os.path.join(root_folder, i)

        try:
            os.mkdir(folder)
        except FileExistsError:
            pass

        config['projects'][f'{i.lower()}_projects_path'] = folder

        print(
            f"{fc.MAGENTA}Created folder for {fc.YELLOW}{i} Projects{fc.BLACK}:{fc.RESET} {folder}")


print("\n\n\nOne more step before we complete the setup.")
print('This is so PYCMD can initialize and delete git repositories.\n\n')
print(fc.LIGHTWHITE_EX +
      "Get your GitHub token from https://github.com/settings/tokens/new")
print("and give it the following scopes:\n")

scopes = {'repo': ['repo:status', 'repo_deployment', 'public_repo',
                   'repo:invite', 'security_events'], 'delete_repo': ['delete_repo']}


for i in scopes:
    print(
        f"{fc.BLACK}•{fc.LIGHTBLUE_EX} {i}{fc.BLACK}: {fc.GREEN}{', '.join(scopes[i])}")
print('\nSet the expiration date to atleast a month or you will be asked to re-authenticate.')
print('You can also do this in the .env file.')
print('\n' + fc.LIGHTWHITE_EX + "Press [Y] to continue.")
response = msvcrt.getch().decode()


if response.lower() == 'n':
    config['is_setup'] = False

else:
    print(fc.LIGHTWHITE_EX + '\nWhat is your GitHub token?')
    github_token = getpass(fc.CYAN + "» " + fc.GREEN)
    with open('.env', 'w') as f:
        f.write(f'GITHUB_TOKEN={github_token}')
        f.close()

# ----Finishing the setup----

# Writing to json
json_location = os.path.abspath('json/config.json')

with open(json_location, 'r') as f:
    data = json.load(f)
    f.close()

data.update(config)

with open(json_location, 'w') as f:
    json.dump(data, f, indent=4)
    f.close()

print(fc.CYAN + '\n\nSetup complete!')
print('\n' + fc.GREEN + "We've (I mean i've) saved everything to the config ;)")
print("Here, have some bread: 🍞👍")


# TODO: Add support for other languages